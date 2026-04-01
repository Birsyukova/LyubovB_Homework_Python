import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    
  
    wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    
    for product_name in products:
        product_xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        wait.until(EC.element_to_be_clickable((By.XPATH, product_xpath))).click()
    

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    
    driver.find_element(By.ID, "first-name").send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Petrov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    
    driver.find_element(By.ID, "continue").click()
    
    total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    total_value = total_text.split('$')[-1]

    print(f"Total value is: {total_value}")
    
    assert total_value == "58.29"  

    driver.quit()

    