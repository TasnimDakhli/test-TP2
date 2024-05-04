# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDemoblazeCategories():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demoblazeCategories(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(866, 1020)
    self.driver.find_element(By.ID, "itemc").click()
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()
    self.driver.find_element(By.LINK_TEXT, "Monitors").click()
    self.driver.find_element(By.ID, "itemc").click()
  
