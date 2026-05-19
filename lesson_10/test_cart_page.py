import pytest
import allure
from selenium import webdriver
from lesson_10.login_page import LoginPage
from lesson_10.product_list_page import ProductListPage
from lesson_10.cart_page import CartPage
from lesson_10.check_out_step_one_page import CheckOutStepOnePage
from lesson_10.check_out_complete_page import CheckOutCompletePage

# Фикстура для запуска и закрытия драйвера


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка перехода к оформлению заказа")
@allure.description("Тест проверяет, что при клике на кнопку 'оформить заказ' произойдет переход на страницу оформления заказа.")
@allure.feature("Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_proceed(driver):
    # Создаем все страницы
    login_page = LoginPage(driver)
    product_list_page = ProductListPage(driver)
    cart_page = CartPage(driver)
    check_out_step_one_page = CheckOutStepOnePage(driver)
    check_out_complete_page = CheckOutCompletePage(driver)

    # Шаг 1: Авторизация
    with allure.step("Авторизация пользователя"):
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    # Шаг 2: Добавление товаров в корзину
    with allure.step("Добавляем продукты в корзину"):
        products = ["Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for product in products:
            product_list_page.add_product_to_cart(product)

    # Шаг 3: Переход в корзину и оформление заказа
    with allure.step("Переходим в корзину"):
        product_list_page.go_to_cart()
    with allure.step("Переходим к оформлению заказа"):
        cart_page.proceed_to_checkout()

    # Шаг 4: Заполняем форму покупателя
    with allure.step("Заполняем форму покупателя"):
        check_out_step_one_page.fill_form_data("Ivan", "Petrov", "123456")
        check_out_step_one_page.submit_form()

    # Шаг 5: Проверка перехода на страницу подтверждения
    with allure.step("Проверяем, что переходим на страницу подтверждения заказа"):
        # Можно добавить проверку URL или наличия элемента
        assert "checkout-step-two" in driver.current_url

    # Шаг 6: Проверяем итоговую цену заказа
    with allure.step("Проверка итоговой стоимости заказа"):
        total_price = check_out_complete_page.get_total_price()
        print(f'Итоговая цена: {total_price}')
        # assert total_price == '$58.29'
