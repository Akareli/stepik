from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(8)
# open browser
driver.get("https://www.mimecast.com/get-a-quote/?utm_medium=semppc&utm_source=googleppc&utm_campaign=quote_request&utm_term=mime%20cast&utm_content=un&gclid=CjwKCAjwxOCRBhA8EiwA0X8hi6Ljq7F8KoPBllqIe-IyH2uNIP_kKc4pVX1EWpEe-qSncYhIZel8RRoChe8QAvD_BwE")

# accept cookies
wait = WebDriverWait(driver, 10)
cookie = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
cookie.click()

# close bot chat pop up
# driver.switch_to.frame((By.NAME, "intercom-launcher-frame"))
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CLASS_NAME, "//div[contains(@class,'intercom-block-paragraph')]")).perform()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Dismiss']"))).click()


# fill out first name field
first_name = driver.find_element(By.ID, "Firame")
first_name.send_keys("a")

# fill out last name field
last_name = driver.find_element(By.ID, "LastName")
last_name.send_keys("For")

# fill out company field
company = driver.find_element(By.ID, "LblCompany")
company.send_keys("M")

# fill out email field
email = driver.find_element(By.ID, "Email")
email.send_keys("ah@fjfd.com")

# fill out telephone field
tel = driver.find_element(By.ID, "LblPhone")
tel.send_keys("76584937")

# select country
selection = Select(driver.find_element(By.ID, "Country"))
selection.select_by_value("nited Kingdom (GB)")

# click "GET MY DEMO"
driver.find_element(By.CSS_SELECTOR, ".mktoButton").click()
