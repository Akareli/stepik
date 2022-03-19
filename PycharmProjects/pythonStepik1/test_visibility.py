# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# import math
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
#
# driver = webdriver.Chrome(service=driver_service)
# BTN_HIDE = (By.ID, "hideButton") #done
# BTN_REMOVED = (By.ID, "removedButton") #done
# BTN_ZERO_WIDTH = (By.ID, "zeroWidthButton")  #done
# BTN_OVERLAPPED = (By.ID, "overlappedButton") #done
# BTN_OPACITY = (By.ID, "transparentButton") #done
# BTN_HIDDEN = (By.ID, "invisibleButton") #done
# BTN_DISPLAY_NONE = (By.ID, "notdisplayedButton")
# BTN_OFFSCREEN = (By.ID, "offscreenButton")
#
# driver.get("http://uitestingplayground.com/visibility")
#
# driver.find_element(*BTN_HIDE).click()
#
# wait = WebDriverWait(driver, 10)
#
# wait.until(EC.invisibility_of_element_located(BTN_REMOVED))
# wait.until(EC.presence_of_element_located(BTN_ZERO_WIDTH))
# overlapped = wait.until(EC.presence_of_element_located(BTN_OVERLAPPED))
# wait.until(EC.presence_of_element_located(BTN_OPACITY))
# driver.execute_script("document.getElementById('invisibleButton').value='Selenium'")
# wait.until(EC.presence_of_element_located(BTN_DISPLAY_NONE))
# wait.until(EC.presence_of_element_located(BTN_OFFSCREEN))
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
# driver.quit()
#
#
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "http://uitestingplayground.com"
visiblty = "/visibility"
removed = (By.ID, "removedButton")
zero_width = (By.ID, "zeroWidthButton")
overlapped = (By.ID, "overlappedButton")
opacity = (By.ID, "transparentButton")


class TestVisibility():

    def setup(self):
        print("start browser for test..")
        self.driver = webdriver.Chrome()

    def teardown(self):
        print("quit browser for test..")
        self.driver.quit()

    def test_should_click_on_hide_button(self):
        self.driver.get(link + visiblty)
        hide = self.driver.find_element(By.ID, "hideButton")
        hide.click()

    def test_should_find_removed_button(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.invisibility_of_element_located(removed))

    def test_should_find_zero_width_button(self):
        buttons = []
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located(zero_width))

    def test_should_find_overlapped_button(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located(overlapped))

    def test_should_find_transparent_button(self)
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located(overlapped))
