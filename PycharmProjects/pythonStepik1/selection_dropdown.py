from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)



driver.get("http://suninjuly.github.io/selects1.html")

num1 = driver.find_element(By.ID, 'num1').text
num2 = driver.find_element(By.ID, 'num2').text
result = str(int(num1) + int(num2))
#
select = Select(driver.find_element(By.TAG_NAME, "select"))

select.select_by_value(result)

driver.find_element(By.XPATH, "//button").click()

print(type(num1))
print(result)



