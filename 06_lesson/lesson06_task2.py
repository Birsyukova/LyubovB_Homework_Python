from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

text_input_locator = (By.ID, "newButtonName")
text_input = driver.find_element(*text_input_locator)
text_input.send_keys("SkyPro")

update_button_locator = (By.ID, "updatingButton")
wait = WebDriverWait(driver, 20)
update_button = wait.until(EC.element_to_be_clickable(update_button_locator))
update_button.click()

updated_button_text_locator = (By.XPATH, "//button[@id='updatingButton' and text()='SkyPro']")
updated_button = wait.until(EC.presence_of_element_located(updated_button_text_locator))

actual_button_text = updated_button.text
expected_button_text = "SkyPro"

print(f"Текст кнопки после обновления: {actual_button_text}")


driver.quit()


