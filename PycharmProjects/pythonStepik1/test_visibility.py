
#
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#
# LINK = "http://uitestingplayground.com"
# VISIBILITY = "/visibility"
# REMOVED = (By.ID, "removedButton")
# ZERO_WIDTH = (By.ID, "zeroWidthButton")
# OVERLAPPED = (By.ID, "overlappedButton")
# OPACITY = (By.ID, "transparentButton")
#
#
# class TestVisibility():
#
#     def setup(self):
#         print("start browser for test..")
#         self.driver = webdriver.Chrome()
#
#     def teardown(self):
#         print("quit browser for test..")
#         self.driver.quit()
#
#     def test_should_click_on_hide_button(self):
#         self.driver.get(link + visiblty)
#         hide = self.driver.find_element(By.ID, "hideButton")
#         hide.click()
#
#     def test_should_find_removed_button(self):
#         self.wait = WebDriverWait(self.driver, 10)
#         self.wait.until(EC.invisibility_of_element_located(removed))
#
#     def test_should_find_zero_width_button(self):
#         buttons = []
#         self.wait = WebDriverWait(self.driver, 10)
#         self.wait.until(EC.presence_of_element_located(zero_width))
#
#     def test_should_find_overlapped_button(self):
#         self.wait = WebDriverWait(self.driver, 10)
#         self.wait.until(EC.presence_of_element_located(overlapped))
#
#     def test_should_find_transparent_button(self):
#         self.wait = WebDriverWait(self.driver, 10)
#         self.wait.until(EC.presence_of_element_located(overlapped))
