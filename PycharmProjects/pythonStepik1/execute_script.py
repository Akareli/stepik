from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")

driver = webdriver.Chrome(service=driver_service)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))




driver.get("http://suninjuly.github.io/execute_script.html")

input_value = driver.find_element(By.ID, "input_value").text

x = calc(input_value)

input_field = driver.find_element(By.ID, "answer")

input_field.send_keys(x)

button = driver.find_element(By.XPATH, '//button')
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.ID, "robotsRule").click()
button.click()





