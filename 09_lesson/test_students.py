import pytest
from sqlalchemy import create_engine, text

# Укажите вашу строку подключения
CONNECTION_STRING = ""

@pytest.fixture
def db_connection():
    engine = create_engine(CONNECTION_STRING)
    connection = engine.connect()
    yield connection
    connection.close()

def test_add_student(db_connection):
    # Добавляем нового студента
    db_connection.execute(
        text("INSERT INTO students (name, age) VALUES (:name, :age)"),
        {'name': 'Ivan', 'age': 20}
    )
    # Проверяем, что студент добавлен
    result = db_connection.execute(
        text("SELECT * FROM students WHERE name=:name AND age=:age"),
        {'name': 'Ivan', 'age': 20}
    ).fetchone()
    assert result is not None, "Студент не был добавлен"
    
    # Удаляем тестового студента
    db_connection.execute(
        text("DELETE FROM students WHERE name=:name AND age=:age"),
        {'name': 'Ivan', 'age': 20}
    )

def test_update_student(db_connection):
    # Создаем студента для обновления
    db_connection.execute(
        text("INSERT INTO students (name, age) VALUES (:name, :age)"),
        {'name': 'Anna', 'age': 22}
    )
    # Получаем его ID с помощью .mappings()
    row = db_connection.execute(
        text("SELECT id FROM students WHERE name=:name"),
        {'name': 'Anna'}
    ).mappings().fetchone()

    student_id = row['id']
    # Обновляем возраст
    db_connection.execute(
        text("UPDATE students SET age=:age WHERE id=:id"),
        {'age': 23, 'id': student_id}
    )
    # Проверяем обновление
    result = db_connection.execute(
        text("SELECT age FROM students WHERE id=:id"),
        {'id': student_id}
    ).mappings().fetchone()
    assert result['age'] == 23

def test_delete_student(db_connection):
    # Создаем студента
    db_connection.execute(
        text("INSERT INTO students (name, age) VALUES (:name, :age)"),
        {'name': 'Test', 'age': 30}
    )
    # Получаем его ID с помощью .mappings()
    row = db_connection.execute(
        text("SELECT id FROM students WHERE name=:name"),
        {'name': 'Test'}
    ).mappings().fetchone()

    student_id = row['id']
    
    # Удаляем студента
    db_connection.execute(
        text("DELETE FROM students WHERE id=:id"),
        {'id': student_id}
    )
    
    # Проверяем, что студент удален
    result = db_connection.execute(
        text("SELECT * FROM students WHERE id=:id"),
        {'id': student_id}
    ).mappings().fetchone()

    assert result is None
