from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ProductListPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы элементов продукта
        self.add_to_cart_buttons = {
            "Sauce Labs Backpack": (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button"),
            "Sauce Labs Bolt T-Shirt": (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button"),
            "Sauce Labs Onesie": (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
        }
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_product_to_cart(self, product_name):
        #Добавляет продукт в корзину
        button = self.driver.find_element(*self.add_to_cart_buttons[product_name])
        button.click()

    def go_to_cart(self):
        #Переходит в корзину
        cart_icon = self.driver.find_element(*self.cart_icon)
        cart_icon.click()