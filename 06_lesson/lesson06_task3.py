from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

image_locator = (By.XPATH, "//div[@class='container']//img[position()=3]") 
wait = WebDriverWait(driver, 30) 

third_image = wait.until(EC.visibility_of_element_located(image_locator))

image_src = third_image.get_attribute("src")

print(f"Значение атрибута src у 3-й картинки: {image_src}")

driver.quit()