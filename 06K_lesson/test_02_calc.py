import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator_with_delay(driver):
    wait = WebDriverWait(driver, 50)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")
    
    button_7 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)"))).click()
    button_plus = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)"))).click()
    button_8 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)"))).click()
    button_equal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning"))).click()
    
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = driver.find_element(By.CLASS_NAME, "screen").text
    
    assert result_text == "15"
    
    print(result_text)

    driver.quit()