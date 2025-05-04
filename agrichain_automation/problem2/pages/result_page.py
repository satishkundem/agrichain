from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.output_text = (By.ID, "outputValue")

    def get_output(self):
        return self.driver.find_element(*self.output_text).text
