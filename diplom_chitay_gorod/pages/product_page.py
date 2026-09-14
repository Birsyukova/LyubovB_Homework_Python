from selenium.webdriver.common.by import By 
from .base_page import BasePage 

class ProductPage(BasePage): 
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="add-to-cart"]') 
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.product-title') 

    def add_to_cart(self): 
        self.click_element(self.ADD_TO_CART_BUTTON) 

    def get_product_title(self): 
        return self.get_element_text(self.PRODUCT_TITLE) 