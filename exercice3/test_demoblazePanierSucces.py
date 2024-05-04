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
class TestDemoblazePanier():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_demoblazePanier(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(1722, 1034)
        self.driver.find_element(By.ID, "cartur").click()
        
        # Récupérer tous les éléments du panier
        items_in_cart = self.driver.find_elements(By.CSS_SELECTOR, ".success")

        # Vérifier et supprimer chaque article si nécessaire
        for item in items_in_cart:
            item_name = item.find_element(By.TAG_NAME, "td").text
            if item_name == "Your item name":  # Remplacez "Your item name" par le nom de votre article
                # Supprimer l'article
                delete_button = item.find_element(By.LINK_TEXT, "Delete")
                delete_button.click()
                # Attendre un court instant pour que l'élément soit supprimé
                time.sleep(1)
                break  # Sortir de la boucle une fois que l'article est supprimé
