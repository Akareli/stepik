from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)

driver.get("http://suninjuly.github.io/alert_accept.html")

button = driver.find_element(By.XPATH, "//button")
button.click()

confirm = driver.switch_to.alert
confirm.accept()

digit = driver.find_element(By.ID, "input_value")
digit = digit.text
x = calc(digit)

input_field = driver.find_element(By.ID,"answer").send_keys(x)

submit = driver.find_element(By.XPATH, '//button').click()

