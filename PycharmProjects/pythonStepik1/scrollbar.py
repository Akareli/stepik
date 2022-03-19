# import unittest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# import math
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class Scrollbar(unittest.TestCase):
#     hidden_btn_id = (By.ID, "hidingButton")
#
#
#     if __name__ == "__main__":
#         unittest.main()
#
#     def __init__(self):
#         self.driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
#         self.driver = webdriver.Chrome(service=self.driver_service)
#
#
#     def test_scrollbar(self):
#         driver = self.driver
#         self.driver.get("http://uitestingplayground.com/scrollbars")
#         hidden = self.driver.find_element(*self.hidden_btn_id)
#         self.driver.execute_script("arguments[0].scrollIntoView();", hidden)
#         self.hidden.click()
#
#     def teardown(self):
#         self.driver.quit()