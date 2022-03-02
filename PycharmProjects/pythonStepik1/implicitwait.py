from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import math
driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")

driver = webdriver.Chrome(service=driver_service)
wait = WebDriverWait(driver, 12)

driver.get("http://suninjuly.github.io/explicit_wait2.html")




wait.until(EC.text_to_be_present_in_element((By.ID,"price"),'100'))

driver.find_element(By.ID, "book").click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = driver.find_element(By.ID,"input_value").text

y = calc(x)

driver.find_element(By.ID, "answer").send_keys(y)
driver.find_element(By.ID,"solve").click()
