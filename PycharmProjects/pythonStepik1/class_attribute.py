from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages import base_page


driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service = driver_service)


CLASS_ATTRIBUTE = (By.CSS_SELECTOR, "a[href='/classattr']")
BTN_PRIMARY = (By.CSS_SELECTOR, "button[class*='btn-primary']")

driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/")
from time import sleep
sleep(2)
attr = driver.find_element(*CLASS_ATTRIBUTE)
attr.click()
sleep(2)
blue = driver.find_element(*BTN_PRIMARY)
blue.click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
driver.quit()


