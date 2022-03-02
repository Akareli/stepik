from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)

driver.get("http://suninjuly.github.io/get_attribute.html")

treasure = driver.find_element(By.ID, 'treasure')
x = treasure.get_attribute("valuex")

y = calc(x)

input_field = driver.find_element(By.ID, "answer")
input_field.send_keys(y)

robot_check = driver.find_element(By.ID,"robotCheckbox").click()

robot_rule = driver.find_element(By.ID, "robotsRule").click()

driver.find_element(By.XPATH, "//button").click()

driver.quit()

