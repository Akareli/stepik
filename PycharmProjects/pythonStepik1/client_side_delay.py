from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CLIENT_SIDE_URL = "http://uitestingplayground.com/clientdelay"
BTN_TRIGGER_CLIENT = (By.ID, "ajaxButton")
TRIGGER_TEXT = (By.CSS_SELECTOR, 'p.bg-success')

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)

driver.get(CLIENT_SIDE_URL)
trigger = driver.find_element(*BTN_TRIGGER_CLIENT)
trigger.click()

wait = WebDriverWait(driver, 16)
actual_text = wait.until(EC.visibility_of_element_located(TRIGGER_TEXT)).text
expected_text = "Data calculated on the client side."
assert actual_text == expected_text, f'The actual text is {actual_text},but should be {expected_text}'

driver.quit()





