import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    '''
    Фикстура для инициализации и завершения работы драйвера
    '''
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

    browser.quit()