import requests
import pytest
import uuid

API_KEY = "jNDA-EM8FOPoQDLgUrQqelliTLnIZKJndjBdfXFEcTtOm+YkV8CZxDps1RkXJ0jg"
BASE_URL = "https://ru.yougile.com"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get_user_id():
    """Получаем ID текущего пользователя"""
    r = requests.get(f"{BASE_URL}/api-v2/users", headers=HEADERS)
    assert r.status_code == 200, f"GET /users failed: {r.text}"
    users = r.json().get("content", [])
    assert users, "Список пользователей пуст"
    return users[0]["id"]


@pytest.fixture(scope="session")
def user_id():
    return get_user_id()


@pytest.fixture
def create_project(user_id):
    payload = {
        "title": "Test Project",        
        "users": {user_id: "admin"}        
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201, f"Fixture failed: {response.text}"
    project_id = response.json()["id"]
    yield project_id
    requests.delete(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)


def test_create_project_positive(user_id):
    payload = {
        "title": "Auto Test Project",
        "users": {user_id: "admin"}
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201, response.text
    assert "id" in response.json()


def test_create_project_negative():
    # Без title — обязательное поле
    payload = {"users": {}}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 400, response.text


def test_update_project_positive(create_project):
    project_id = create_project
    payload = {"title": "Updated Project Title"}
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=payload
    )
    assert response.status_code == 200, response.text


def test_update_project_negative():
    fake_id = str(uuid.uuid4())  # валидный UUID, которого нет
    payload = {"title": "Invalid update"}
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{fake_id}", headers=HEADERS, json=payload
    )
    assert response.status_code == 404, response.text


def test_get_project_positive(create_project):
    project_id = create_project
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200, response.text
    assert response.json()["id"] == project_id


def test_get_project_negative():
    fake_id = str(uuid.uuid4())
    response = requests.get(f"{BASE_URL}/api-v2/projects/{fake_id}", headers=HEADERS)
    assert response.status_code == 404, response.text
