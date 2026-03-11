import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Импортируем TimeoutException

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

def test_fill_and_validate_form(browser):
    # Переходим на страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(browser, 15)

    # Заполняем форму
    browser.find_element(By.NAME, "first-name").send_keys("Иван")
    browser.find_element(By.NAME, "last-name").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input").send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input").send_keys("+7985899998787")
    browser.find_element(By.NAME, "zip-code").clear()  # Оставляем пустым
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "job-position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button")
    submit_button.click()

    #Ожидаем сообщение об успешном прохождении валидации
    try:
        wait.until(EC.presence_of_element_located((By.NAME, "validation-message")))
    except TimeoutException:
        print("сообщение об успешной валидации не найдено.")
        assert False 


    #Проверяем стили выделений
    fields_to_check = ["first-name", "last-name", "address", "email", "phone-number", "city", "country", "job-position", "company"]
    for field_id in fields_to_check:
        element = browser.find_element(By.NAME, field_id)
        color = element.value_of_css_property("border-bottom-color")
        assert "#4CAF50" in color.lower(), f"Поле '{field_id}' не подсвечено зеленым цветом."

    # Проверяем, что поле ZIP подсвечено красным
    zip_code_field = browser.find_element(By.NAME, "zip-code")
    zip_color = zip_code_field.value_of_css_property("border-bottom-color")
    assert "#FFCDD2" in zip_color.lower(), "Поле 'ZIP Code' не подсвечено красным цветом."


    