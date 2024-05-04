import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemoblazeCategories():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_demoblazeCategories(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(866, 1020)
        
        # Define variables
        category = "Laptops"
     
        
        # Click on the categories
        self.driver.find_element(By.ID, "itemc").click()
        self.driver.find_element(By.LINK_TEXT, category).click()
        
        # Assertion to verify navigation to laptops category
        assert self.driver.current_url == "https://www.demoblaze.com/#", "Failed to navigate to  {category} category."
        
       
