import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


class TestBookSearch:

    def search(self, driver: WebDriver, query: str) -> str:
        driver.get("https://www.chitai-gorod.ru")

        wait = WebDriverWait(driver, 30)

        # несколько селекторов для поля поиска
        search_field = None
        selectors = [
            "input[placeholder*='Поиск']",
            "input[type='search']",
            "input[class*='search']",
            "input[id*='search']",
            "input[name*='search']",
            ".search input",
            ".header-search input",
            "input[data-testid*='search']"
        ]

        for selector in selectors:
            try:
                search_field = wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                )
                break
            except:
                continue

        if not search_field:
            # попытка - найти любой input
            inputs = driver.find_elements(By.TAG_NAME, "input")
            for input_elem in inputs:
                if input_elem.is_displayed():
                    search_field = input_elem
                    break

        if not search_field:
            raise Exception("Не удалось найти поле поиска")

        search_field.clear()
        search_field.send_keys(query)

        
        search_field.send_keys(Keys.ENTER)

        
        time.sleep(5)  # Дополнительное ожидание

        
        body = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        return body.text.lower()

    @allure.epic("UI Тестирование")
    @allure.feature("Поиск книжной информации")
    @allure.title("Поиск книги по заголовку")
    def test_by_name(self, driver: WebDriver):
        result = self.search(driver, "капитанская")
        assert "капитанская" in result

    @allure.epic("UI Тестирование")
    @allure.feature("Поиск книжной информации")
    @allure.title("Поиск автора")
    def test_by_author(self, driver: WebDriver):
        result = self.search(driver, "пушкин")
        assert "пушкин" in result

    @allure.epic("UI Тестирование")
    @allure.feature("Поиск книжной информации")
    @allure.title("Поиск книги на английском языке")
    def test_by_name_language_english(self, driver: WebDriver):
        result = self.search(driver, "The Captain's Daughter")
        assert (
            "captain" in result
            or "результат" in result
            or "ничего не найдено" in result
        )

    @allure.epic("UI Тестирование")
    @allure.feature("Поиск книжной информации")
    @allure.title("Поиск книги с символами вместо названия")
    def test_negative_by_symbols(self, driver: WebDriver):
        result = self.search(driver, "@#$%^&*()")
        assert (
            "@#$%^&*()" in result
            or "результат" in result
            or "ничего не найдено" in result
        )

    @allure.epic("UI Тестирование")
    @allure.feature("Поиск книжной информации")
    @allure.title("Поиск книги на тайском языке")
    def test_negative_by_language_thai(self, driver: WebDriver):
        result = self.search(driver, "กัปตัน")
        assert (
            "กัปตัน" in result
            or "не дал результатов" in result
            or "ничего не найдено" in result
        )
