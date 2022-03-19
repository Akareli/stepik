import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")

class TestSelectors(unittest.TestCase):
    def test_selector1(self):
        # driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
        self.driver = webdriver.Chrome(service=driver_service)

        self.driver.get("http://suninjuly.github.io/registration1.html")

        first = self.driver.find_element(By.XPATH, "//div[contains(@class, 'first_block')]/div/input[contains(@class,'first')]")
        first.send_keys("Anna")

        last = self.driver.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group second_class']/input")
        last.send_keys("Karelina")

        email = self.driver.find_element(By.XPATH, "//div[contains(@class, 'first_block')]/div/input[contains(@class,'third')]")
        email.send_keys("annette@list.ru")

        self.driver.find_element(By.XPATH, "//button").click()

        text = self.driver.find_element(By.TAG_NAME, "h1").text
        assert text == "Congratulations! You have successfully registered!", f'The actuals text is {text}'

    def test_selector2(self):
        # driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
        self.driver = webdriver.Chrome(service=driver_service)

        self.driver.get("http://suninjuly.github.io/registration2.html")

        first = self.driver.find_element(By.XPATH, "//div[contains(@class, 'first_block')]/div/input[contains(@class,'first')]")
        first.send_keys("Anna")

        last = self.driver.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group second_class']/input")
        last.send_keys("Karelina")

        email = self.driver.find_element(By.XPATH, "//div[contains(@class, 'first_block')]/div/input[contains(@class,'third')]")
        email.send_keys("annette@list.ru")

        self.driver.find_element(By.XPATH, "//button").click()

        text = self.driver.find_element(By.TAG_NAME, "h1").text
        assert text == "Congratulations! You have successfully registered!", f'The actuals text is {text}'

    # def test_abs2(self):
    #     self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
#
#
# def test_abs1():
#     # assert abs(-42) == 42, "Should be absolute value of a number"
#     driver_service = Service(executable_path="/Users/annakarelina/PycharmProjects/pythonStepik1/chromedriver")
#
#     driver = webdriver.Chrome(service=driver_service)
#
#     driver.get("http://suninjuly.github.io/registration2.html")
#
#     first = driver.find_element(By.XPATH, "//div[contains(@class, 'first_block')]/div/input[contains(@class,'first')]")
#     first.send_keys("Anna")
#
#     last = driver.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group second_class']/input")
#     last.send_keys("Karelina")
#
#     email = driver.find_element(By.XPATH, "//div[contains(@class, 'first_block')]/div/input[contains(@class,'third')]")
#     email.send_keys("annette@list.ru")
#
#     button = driver.find_element(By.XPATH, "//button").click()
#
#     text = driver.find_element(By.TAG_NAME, "h1").text
#     assert text == "Congratulations! You have successfully registered!", f'The actuals text is {text}'
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")
#

