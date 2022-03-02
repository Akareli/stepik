from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")

driver = webdriver.Chrome(service=driver_service)

driver.get("http://suninjuly.github.io/redirect_accept.html")

submit = driver.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']").click()


cur_window = driver.current_window_handle


driver.switch_to.window(driver.window_handles[1])

digit = driver.find_element(By.ID,"input_value").text
x = calc(digit)

input_field = driver.find_element(By.ID, "answer")

input_field.send_keys(x)

driver.find_element(By.XPATH, "//button").click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)






