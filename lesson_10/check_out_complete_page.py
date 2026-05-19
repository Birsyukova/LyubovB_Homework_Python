from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CheckOutCompletePage:
    """
    Страница завершения оформления заказа.

    Атрибуты:
        driver (WebDriver): Объект драйвера Selenium.
        total_amount (tuple): Локатор элемента, отображающего итоговую сумму.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы завершения оформления заказа.

        :param driver: WebDriver - драйвер браузера.
        """
        self.driver: WebDriver = driver
        self.total_amount: tuple = (By.CLASS_NAME, 'summary_total_label')

    @allure.step("Получение общей суммы заказа")
    def get_total_price(self) -> str:
        """
        Получает общую сумму заказа из страницы.

        :return: Строка с суммой.
        """
        total_text = self.driver.find_element(*self.total_amount).text.strip()
        # Assuming формат: "Total: $123.45"
        return total_text.split(':')[1].strip()
