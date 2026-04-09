from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckOutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.total_amount = (By.CLASS_NAME, 'summary_total_label')

    def get_total_price(self):
        #Получает общую сумму заказа
        return self.driver.find_element(*self.total_amount).text.strip().split(':')[1].strip()