from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")

driver = webdriver.Chrome(service=driver_service)

try:

    driver.get("http://suninjuly.github.io/simple_form_find_task.html")

    input1 = driver.find_element(By.TAG_NAME,"input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME,"last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME,"form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID,"country" )
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR,"#submit_button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()