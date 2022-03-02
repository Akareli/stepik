from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver.common.by import By
import math

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
# driver = webdriver.Chrome(service=driver_service)



driver.get("http://suninjuly.github.io/math.html")
driver.maximize_window()
driver.implicitly_wait(4)

element = driver.find_element(By.ID, 'input_value')
value_x = element.text
y = calc(value_x)

input_field = driver.find_element(By.ID, 'answer')
input_field.send_keys(y)

checkbox = driver.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radiobutton = driver.find_element(By.ID, 'robotsRule')
radiobutton.click()

submitbutton = driver.find_element(By.XPATH, "//button").click()




