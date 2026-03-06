from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.XPATH, "//input[@type='number']")

input_field.send_keys("12345")
print("Введено: 12345")

input_field.clear()
print("Поле очищено.")

input_field.send_keys("54321")
print("Введено: 54321")

driver.quit()
