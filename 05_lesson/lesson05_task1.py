from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/classattr")
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()

driver.quit()