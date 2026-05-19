from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    """
    Страница калькулятора.
    """

    # Локаторы элементов
    DELAY_FIELD_LOCATOR: tuple = (By.ID, 'delay')
    RESULT_SCREEN_LOCATOR: tuple = (By.CLASS_NAME, 'screen')
    BUTTONS_LOCATORS: dict = {
        '7': (By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)'),
        '+': (By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)'),
        '8': (By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)'),
        '=': (By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning'),
    }

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> 'CalculatorPage':
        """
        Открывает страницу калькулятора.
        """
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        return self

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds: int) -> 'CalculatorPage':
        delay_field: WebElement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DELAY_FIELD_LOCATOR))
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    @allure.step("Нажатие кнопки '{label}'")
    def click_button(self, label: str) -> 'CalculatorPage':
        locator = self.BUTTONS_LOCATORS.get(label)
        if not locator:
            raise ValueError(f"Клавиша '{label}' не найдена.")
        button: WebElement = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        button.click()
        return self
    
    @allure.step("Получение результата")
    def get_result(self) -> str:
        screen: WebElement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RESULT_SCREEN_LOCATOR)
        )
        result_text: str = screen.text.strip()
        print(f"Контент `div.screen`: '{result_text}'")  # Для проверки
        return result_text
