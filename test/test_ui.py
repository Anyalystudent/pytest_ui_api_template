from Pages.MainPage import MainPage
import allure


@allure.story("Поиск товара")
@allure.feature("READ")
@allure.title("Поиск товара через строку поиска")
def test_search_product(driver):
    """
    Тест на поиск заданного товара через строку поиска
    """
    search_query = "молоко"
    main = MainPage(driver)
    main.open()
    main.search_string(search_query)

    with allure.step("Проверить, что результаты отобразились"):
        assert main.is_results_displayed(), "Результаты поиска не найдены"
    with allure.step("Получить список текстов результатов"):
        results = main.get_search_results()
    with allure.step("Проверить, список результатов поиска больше ноля"):
        assert len(results) > 0, "Нет результатов поиска"
    print(f"Найдено {len(results)} результатов")
    print(f"Первый результат: {results[0]}")


@allure.story("Поиск товара")
@allure.feature("READ")
@allure.title("Поиск товара через выбор магазина")
def test_search_product_in_shop(driver):
    """
    Тест на поиск товара через выбор магазина
    """
    search_query = "мороженое"
    main = MainPage(driver)
    main.open()

    main.search_in_shop(search_query)
    first_product = main.get_first_result_text()
    with allure.step("Проверить, что получен что первый товар"):
        assert first_product is not None


@allure.story("Поиск товара")
@allure.feature("READ")
@allure.title("Поиск несуществующего товара")
def test_search_not_existent_product(driver):
    """
    тест на поиск несуществующего товара
    """
    search_query = "ыгпнщ"
    main = MainPage(driver)
    main.open()
    main.search_string(search_query)
    with allure.step("Проверить, что результатов нет"):
        assert main.has_no_results()


@allure.story("Поиск товара")
@allure.feature("READ")
@allure.title("Поиск пустой строки")
def test_search_empty(driver):
    """
    тест на поиск пустой строки
    """
    search_query = ""
    main = MainPage(driver)
    main.open()
    main.search_string(search_query)
    with allure.step("Проверить сообщение при пустом поиске"):
        assert main.search_empty_results()


@allure.story("Поиск ресторана")
@allure.feature("READ")
@allure.title("Поиск ресторана через строку поиска")
def test_search_restaurant(driver):
    """
    Тест на поиск ресторана
    """
    search_query = "Бургер Кинг"
    main = MainPage(driver)
    main.open()
    main.search_restaurant(search_query)
    with allure.step("Проверить, что отобразились результаты поиска ресторана"):
        assert main.is_results_restaurant_displayed(), "Результаты поиска не найдены"
