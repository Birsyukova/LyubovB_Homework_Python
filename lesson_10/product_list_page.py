from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ProductListPage:
    """
    Страница со списком продуктов.

    Атрибуты:
        driver (WebDriver): Объект драйвера Selenium.
        add_to_cart_buttons (dict): Словарь локаторов кнопок добавления товаров.
        cart_icon (tuple): Локатор иконки корзины.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы листинга товаров.

        :param driver: WebDriver - драйвер браузера.
        """
        self.driver: WebDriver = driver
        self.add_to_cart_buttons: dict = {
            "Sauce Labs Backpack": (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button"),
            "Sauce Labs Bolt T-Shirt": (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button"),
            "Sauce Labs Onesie": (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
        }
        self.cart_icon: tuple = (By.CLASS_NAME, 'shopping_cart_link')

    @allure.step("Добавляем товар в корзину: {product_name}")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        :param product_name: Название продукта
        """
        with allure.step(f"Добавляем продукт: {product_name}"):
            button = self.driver.find_element(
                *self.add_to_cart_buttons[product_name])
            button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        cart_icon = self.driver.find_element(*self.cart_icon)
        cart_icon.click()
