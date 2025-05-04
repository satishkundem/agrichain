from selenium import webdriver
import pytest
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def setup(browser):
    if browser == 'edge':
        service = Service(executable_path=r"../drivers/msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    else:
        service = Service(executable_path=r"../drivers/chromedriver.exe")
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()