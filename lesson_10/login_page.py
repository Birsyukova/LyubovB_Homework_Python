from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class LoginPage:
    """
    Страница авторизации на сайте.

    Атрибуты:
        driver (WebDriver): Объект драйвера Selenium.
        username_field (tuple): Локатор поля ввода логина.
        password_field (tuple): Локатор поля ввода пароля.
        login_button (tuple): Локатор кнопки входа.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы логина.

        :param driver: WebDriver - драйвер браузера.
        """
        self.driver: WebDriver = driver
        self.username_field: tuple = (By.ID, 'user-name')
        self.password_field: tuple = (By.ID, 'password')
        self.login_button: tuple = (By.ID, 'login-button')

    @allure.step("Открываем страницу авторизации")
    def open(self) -> None:
        """
        Переходит на страницу авторизации.
        """
        self.driver.get('https://www.saucedemo.com/')

    @allure.step("Вводим логин: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: логин пользователя
        """
        self.driver.find_element(*self.username_field).send_keys(username)

    @allure.step("Вводим пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: пароль пользователя
        """
        self.driver.find_element(*self.password_field).send_keys(password)

    @allure.step("Кликаем кнопку входа")
    def click_login(self) -> None:
        """

        Нажимает кнопку входа.
        """
        self.driver.find_element(*self.login_button).click()
