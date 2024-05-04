import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemoblazeAjoutPanier():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_demoblazeAjoutPanier(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(1722, 1034)
        
        # Define variables
        product_name = "Samsung galaxy s6"
        expected_message = "Product added"
        
        # Click on the product
        self.driver.find_element(By.LINK_TEXT, product_name).click()
        
        # Click on "Add to cart"
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        
        # Assertion to verify product added message
        alert_text = self.driver.switch_to.alert.text
        assert alert_text == expected_message, f"Expected message '{expected_message}' not found. Actual message: {alert_text}"
