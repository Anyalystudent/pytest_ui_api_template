from selenium.webdriver.common.by import By
import requests

from pytest_ui_api_template.conftest import driver


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://market-delivery.yandex.ru")

    def search(self, title):
        my_headers = {
            'text': title,
            'location': {
                'longitude': 37.59217698696895,
                'latitude': 55.750078863243985
            }
        }
        resp = requests.post(self._driver + '/eats/v1/full-text-search/v1/search', headers=my_headers)
        return resp














        #self._driver.find_element(By.CSS_SELECTOR, "input#id_1").send_keys(term)
        #self._driver.find_element(By.CSS_SELECTOR, ".UiKitButton_size-l_4a538d41").click()