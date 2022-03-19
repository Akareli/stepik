class Page():

    def __init__(self, driver):
        self.driver = driver


    def open_url(self, url):
        self.driver.get(url)


    def input_text(self,*locator,text:str):
        e = self.driver.find_element(*locator)
        e.send_keys(text)


    def click_element(self,*locator):
        self.driver.find_element(*locator).click()


    def verify_result_text(self):
        pass