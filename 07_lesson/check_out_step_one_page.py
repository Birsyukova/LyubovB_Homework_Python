from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CheckOutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')

    def fill_form_data(self, first_name, last_name, postal_code):
        #Заполняет форму доставки
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def submit_form(self):
        #Отправляет заполненную форму
        continue_btn = self.driver.find_element(*self.continue_button)
        continue_btn.click()