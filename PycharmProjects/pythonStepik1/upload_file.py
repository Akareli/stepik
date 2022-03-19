import os


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
driver = webdriver.Chrome(service=driver_service)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "I_got_an_offer_on_ 23_of_March_2022"
file_path = os.path.join(current_dir,file_name)
driver.get("https://demo.guru99.com/test/upload/")
s = driver.find_element(By.ID, "uploadfile_0")
s.send_keys(file_path)
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitbutton").click()
actual_text = driver.find_element(By.CSS_SELECTOR,"h3 center").get_attribute("center")
assert actual_text == "1 file has been successfully uploaded.", f'The actual text is {actual_text}'
driver.quit()


