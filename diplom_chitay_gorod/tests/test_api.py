import requests
import allure
from conftest import BASE_URL, HEADERS

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
def test_api_book_by_author():
    response = requests.get(f"{BASE_URL}search/product?phrase=Булгаков", headers=HEADERS)
    assert response.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
def test_api_book_by_title():
    response = requests.get(f"{BASE_URL}search/product?phrase=Моби Дик", headers=HEADERS)
    assert response.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
def test_search_by_language_english():
    response = requests.get(f"{BASE_URL}search/product?phrase=Moby Dick", headers=HEADERS)
    assert response.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
def test_negative_api_japanese():
    response = requests.get(f"{BASE_URL}search/product?phrase=人で座ってください", headers=HEADERS)
    assert response.status_code == 422

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
def test_negative_api_empty_search():
    response = requests.get(f"{BASE_URL}search/product?phrase=", headers=HEADERS)
    assert response.status_code == 400

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
def test_negative_api_no_auth():
    response = requests.get(f"{BASE_URL}search/product?phrase=Moby Dick")  # без headers
    assert response.status_code == 403