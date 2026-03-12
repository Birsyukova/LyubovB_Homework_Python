from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def open(self):
        #Переход на страницу авторизации
        self.driver.get('https://www.saucedemo.com/')

    def enter_username(self, username):
        #Ввод имени пользователя
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        #Ввод пароля
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        #Кликает на кнопку входа
        self.driver.find_element(*self.login_button).click()