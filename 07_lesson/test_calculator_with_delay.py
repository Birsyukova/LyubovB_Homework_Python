import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator_with_delay(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)
    
    # Выполняем последовательность нажатия кнопок
    page.click_button('7').click_button('+').click_button('8').click_button('=')
    
    # Ожидаем появления правильного результата
    wait = WebDriverWait(driver, 50)
    wait.until(lambda d: page.get_result() == '15')
    
    # Проверяем, что результат действительно равен 15
    result = page.get_result()
    assert result == '15', f'Результат отличается от ожидаемого ("15"), фактическое значение: {result}'