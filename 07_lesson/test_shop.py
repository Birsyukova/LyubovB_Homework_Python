import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from login_page import LoginPage
from product_list_page import ProductListPage
from cart_page import CartPage
from check_out_step_one_page import CheckOutStepOnePage
from check_out_complete_page import CheckOutCompletePage

# Фикстура для запуска и закрытия драйвера
@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    product_list_page = ProductListPage(driver)
    cart_page = CartPage(driver)
    check_out_step_one_page = CheckOutStepOnePage(driver)
    check_out_complete_page = CheckOutCompletePage(driver)

    # Шаг 1: Авторизация
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Шаг 2: Добавление продуктов в корзину
    products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for product in products:
        product_list_page.add_product_to_cart(product)

    # Шаг 3: Переход в корзину и оформление заказа
    product_list_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # Шаг 4: Заполнение формы покупателя
    check_out_step_one_page.fill_form_data("Ivan", "Petrov", "123456")
    check_out_step_one_page.submit_form()

    # Шаг 5: Проверяем итоговую цену заказа
    total_price = check_out_complete_page.get_total_price()
    print(f'Итоговая цена: ${total_price}')

    # Убедимся, что итоговая сумма верна
    assert total_price == '$58.29'