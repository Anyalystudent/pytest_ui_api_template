from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://market-delivery.yandex.ru/")

    def search(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input#id_1").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, ".UiKitButton_size-l_4a538d41").click()