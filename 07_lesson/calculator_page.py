from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = None
        self.result_screen = None
        self.buttons = {}
        
    # Локаторы элементов
    DELAY_FIELD_LOCATOR = (By.ID, 'delay')
    RESULT_SCREEN_LOCATOR = (By.CLASS_NAME, 'screen')
    BUTTONS_LOCATORS = {
        '7': (By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)'),
        '+': (By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)'),
        '8': (By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)'),
        '=': (By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning'),
    }

    def open(self):
        #Открывает страницу калькулятора
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        return self

    def set_delay(self, seconds):
        #Устанавливает задержку отображения результата
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DELAY_FIELD_LOCATOR))
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, label):
        #Нажатие на клавишу калькулятора
        locator = self.BUTTONS_LOCATORS.get(label)
        if not locator:
            raise ValueError(f"Клавиша '{label}' не найдена.")
        
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        button.click()
        return self

    def get_result(self):
        #Получение текущего значения экрана калькулятора
        screen = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RESULT_SCREEN_LOCATOR))
        return screen.text.strip()