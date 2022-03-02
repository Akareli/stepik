import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)



driver.get("http://suninjuly.github.io/file_input.html")

directory = '/Users/annakarelina/PycharmProjects/pythonStepik1/texts'
file_name = 'anna.txt'
file_path = os.path.join(directory,file_name)

first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys("Anna")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Karelina")

email = driver.find_element(By.NAME, "email")
email.send_keys("anna@list.ru")

file = driver.find_element(By.ID, "file")
file.send_keys(file_path)

submit = driver.find_element(By.TAG_NAME, 'button').click()
