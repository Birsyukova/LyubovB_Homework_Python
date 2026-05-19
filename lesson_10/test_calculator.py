import allure
from selenium import webdriver
import time
from lesson_10.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка сложения")
@allure.title("Сложение 7 + 8 = 15")
@allure.description("Тест проверяет выполнение операции сложения и отображение правильного результата")
@allure.severity(allure.severity_level.CRITICAL)
def test_addition():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    try:
        with allure.step("Открываем страницу калькулятора"):
            calculator.open()

        with allure.step("Устанавливаем задержку 45 секунд"):
            calculator.set_delay(45)

        with allure.step("Вводим выражение 7 + 8 ="):
            calculator.click_button('7') \
                      .click_button('+') \
                      .click_button('8') \
                      .click_button('=')

        time.sleep(50)
        with allure.step("Проверяем результат"):
            result = calculator.get_result()
            print(f"Полученный результат: {result}")
            assert result == "15", f"Ожидаемый результат 15, но получен {result}"
    finally:
        driver.quit()
