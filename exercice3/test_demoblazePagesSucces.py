from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoblazePages():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_demoblazePages(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(1722, 1034)
        
        # Clicking on "Contact" link
        self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        
        # Closing the modal
        self.driver.find_element(By.CSS_SELECTOR, "#exampleModal .btn-secondary").click()
        
        # Clicking on "About us" link
        self.driver.find_element(By.LINK_TEXT, "About us").click()

        # Waiting for the video player to be clickable
        try:
            video_player = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".vjs-big-play-button")))
            video_player.click()
        except:
            print("Failed to find and click on the video player.")

        # Continue with the rest of your test steps
        # For example:
        # self.driver.find_element(By.CSS_SELECTOR, ".vjs-progress-control").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#videoModal .btn").click()
        # self.driver.find_element(By.ID, "cartur").click()
        # self.driver.find_element(By.ID, "login2").click()
        # etc.


