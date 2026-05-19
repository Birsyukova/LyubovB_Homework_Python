from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class CheckOutStepOnePage:
    """
    Страница этапа один оформления заказа.

    Атрибуты:
        driver (WebDriver): Объект драйвера Selenium.
        first_name_input (tuple): Локатор поля ввода имени.
        last_name_input (tuple): Локатор поля ввода фамилии.
        postal_code_input (tuple): Локатор поля почтового индекса.
        continue_button (tuple): Локатор кнопки продолжить.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы этапа один.

        :param driver: WebDriver - драйвер браузера.
        """
        self.driver: WebDriver = driver
        self.first_name_input: tuple = (By.ID, 'first-name')
        self.last_name_input: tuple = (By.ID, 'last-name')
        self.postal_code_input: tuple = (By.ID, 'postal-code')
        self.continue_button: tuple = (By.ID, 'continue')

    @allure.step("Заполняем форму доставки")
    def fill_form_data(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму доставки.

        :param first_name: Имя
        :param last_name: Фамилия
        :param postal_code: Почтовый индекс
        """
        with allure.step("Вводим имя"):
            self.driver.find_element(
                *self.first_name_input).send_keys(first_name)
        with allure.step("Вводим фамилию"):
            self.driver.find_element(
                *self.last_name_input).send_keys(last_name)
        with allure.step("Вводим почтовый индекс"):
            self.driver.find_element(
                *self.postal_code_input).send_keys(postal_code)

    @allure.step("Отправляем форму")
    def submit_form(self) -> None:
        """
        Нажимает кнопку продолжения.
        """
        continue_btn: WebElement = self.driver.find_element(
            *self.continue_button)
        continue_btn.click()
