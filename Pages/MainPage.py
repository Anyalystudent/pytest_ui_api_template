import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver




class MainPage:
    '''
    Локаторы для главной страницы
    '''
    INPUT = (By.XPATH, '//*[@data-testid="search-input"]')
    SEARCH_BUTTON = (By.XPATH, '//span[text()="Найти"]')
    PRODUCT_NAME = (By.XPATH, '//div[@data-testid="product-card-name"]')
    NO_RESULTS_MESSAGE = (By.XPATH, '//h1[text()="Ничего не нашли, но есть:"]')
    EMPTY_MESSAGE = (By.XPATH, '//h2[text()="Часто ищут"]')
    RESTAURANT_NAME = (By.XPATH, '//span[@data-testid="place-header-title"]')
    '''
    Локаторы для магазина
    '''
    SHOP_LAVKA = (By.CSS_SELECTOR, '[data-place-slug="yandeks_lavka"]')
    CAROUSEL_ITEMS = (By.CSS_SELECTOR, '[data-carousel-item="true"]')
    PRODUCT_NAME_IN_SHOP = (By.CSS_SELECTOR, '[data-testid="product-card"] h3')
    LABEL_LAVKA = (By.CSS_SELECTOR, '[alt="Лого Яндекс Лавка"]')

    def __init__(self, driver):
        """
        Конструктор класса MainPage
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self._driver = driver
        self.url="https://market-delivery.yandex.ru"
        self.wait = WebDriverWait(self._driver, 25)

    @allure.step("UI. Открытие страницы браузера")
    def open(self):
        '''
        Открывает браузер
        '''
        self._driver.get(self.url)

    @allure.step("UI. Поиск товара через строку поиска")
    def search_string(self, title):
        '''
        Выполняет поиск заданного товара через строку поиска
        :param title: str - название товара
        '''
        input_field = (self.wait.until(EC.element_to_be_clickable(self.INPUT)))
        input_field.clear()
        input_field.send_keys(title)

        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()
        # ждем загрузки результатов или в противном случае сообщения, что ничего не найдено
        try:
            return self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME))
        except:
            return False

    @allure.step("UI. Поиск товара через магазин")
    def search_in_shop(self, title):
        '''
        Выполняет поиск товара в заданном магазине
        :param title: str - название товара
        '''
        shop = self.wait.until(EC.visibility_of_element_located(self.SHOP_LAVKA))
        shop.click()
        self._driver.switch_to.window(self._driver.window_handles[-1])
        time.sleep(10)
        input_field = (self.wait.until(EC.element_to_be_clickable(self.INPUT)))
        input_field.clear()
        input_field.send_keys(title)
        input_field.send_keys(Keys.ENTER)
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME_IN_SHOP))

    @allure.step("UI. Проверка отображения результатов")
    def is_results_displayed(self):
        '''
        Проверяет, отобразились ли результаты
        '''
        try:
            return self._driver.find_element(*self.PRODUCT_NAME).is_displayed()
        except:
            return False

    @allure.step("UI. Получение списка текста результатов")
    def get_search_results(self):
        '''
        Возвращает список текстов результатов
        '''
        results = self._driver.find_elements(*self.PRODUCT_NAME)
        return [result.text for result in results if result.text]

    @allure.step("UI. Получение текста первого результата")
    def get_first_result_text(self):
        '''
        Возвращает текст первого результата
        '''
        results = self._driver.find_elements(*self.PRODUCT_NAME_IN_SHOP)
        return results[0].text

    @allure.step("UI. Проверка отсутствия результата")
    def has_no_results(self):
        '''
        Проверяет, что результатов нет
        '''
        try:
            return self._driver.find_element(*self.NO_RESULTS_MESSAGE).is_displayed()
        except:
            return False

    @allure.step("UI. Проверка результата при пустом запросе")
    def search_empty_results(self):
        '''
        Проверяет сообщение при пустом поиске
        '''
        try:
            return self._driver.find_element(*self.EMPTY_MESSAGE).is_displayed()
        except:
            return False

    @allure.step("UI. Поиск ресторана через строку поиска")
    def search_restaurant(self, title):
        '''
        Выполняет поиск заданного ресторана через строку поиска
        :param title: str - название ресторана
        '''
        input_field = (self.wait.until(EC.element_to_be_clickable(self.INPUT)))
        input_field.clear()
        input_field.send_keys(title)

        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()
        # ждем загрузки результатов или в противном случае сообщения, что ничего не найдено
        try:
            return self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME))
        except:
            return False

    @allure.step("UI. Проверка отображения результатов поиска ресторанов")
    def is_results_restaurant_displayed(self):
        '''
        Проверяет, отобразились ли результаты
        '''
        try:
            return self._driver.find_element(*self.RESTAURANT_NAME).is_displayed()
        except:
            return False






