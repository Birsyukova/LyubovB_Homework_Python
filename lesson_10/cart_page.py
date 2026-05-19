from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class CartPage:
    """
    Страница корзины магазина.

    Атрибуты:
        driver (WebDriver): Объект драйвера Selenium.
        checkout_button (tuple): Локатор кнопки оформления заказа.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины.
        :param driver: WebDriver - драйвер браузера.
        """
        self.driver: WebDriver = driver
    # Исправленный локатор: ищем по id='checkout'
        self.checkout_button: tuple = (By.ID, "checkout")

    @allure.step("Переход к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """
        Нажать на кнопку 'Оформить заказ' для перехода к оформлению.

        :return: None
        """
    # Находим кнопку по локатору
        checkout_btn: WebElement = self.driver.find_element(
            *self.checkout_button)
    # Кликаем на кнопку
        checkout_btn.click()
