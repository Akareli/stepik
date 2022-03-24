from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestAjax():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 16)
        print("start browser for test..")

    def teardown(self):
        print("quit browser for test")
        self.driver.quit()

    def test_should_open_page(self):
        self.driver.get("http://uitestingplayground.com/ajax")
        self.wait.until(EC.url_contains("http://uitestingplayground.com/ajax"))

    def test_should_click_ajax_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton"))).click()


    def test_should_wait_before_clicking_text(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "content .bg-success"))).click()


