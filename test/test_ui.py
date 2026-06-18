from Pages.MainPage import MainPage
import time


def test_search_product(driver):
    '''
    Тест на поиск заданного товара через строку поиска
    '''
    search_query = 'молоко'
    main = MainPage(driver)
    main.open()
    main.search_string(search_query)

    # проверяем, что результаты отобразились
    assert main.is_results_displayed(), "Результаты поиска не найдены"

    # получаем список текстов результатов
    results = main.get_search_results()
    assert len(results) > 0, "Нет результатов поиска"
    print(f"Найдено {len(results)} результатов")
    print(f"Первый результат: {results[0]}")

    # Проверяем, что хотя бы один результат содержит слово "{search_query}"
    # found = any('молоко' in result.lower() for result in results)
    # assert found, f"Ни один результат не содержит '{search_query}'"

def test_search_product_in_shop(driver):
    '''
    Тест на поиск товара через выбор магазина
    '''
    search_query = 'мороженое'
    main = MainPage(driver)
    main.open()

    main.search_shop(search_query)
    first_product = main.get_first_result_text()
    print(f"Первый результат: {first_product}")


def test_search_non_existent_product(driver):
    '''
    тест на поиск несуществующего товара
    '''
    search_query = 'ыгпнщ'
    main = MainPage(driver)
    main.open()
    main.search_string(search_query)

    assert  main.has_no_results()

def test_search_empty(driver):
    '''
    тест на поиск пустой строки
    '''
    search_query = ''
    main = MainPage(driver)
    main.open()
    main.search_string(search_query)

    assert main.search_empty_results()

def test_search_restaurant(driver):
    '''
    Тест на поиск ресторана
    '''
    search_query = 'Бургер Кинг'
    main = MainPage(driver)
    main.open()
    main.search_restaurant(search_query)

    # проверяем, что результаты отобразились
    assert main.is_results_restaurant_displayed(), "Результаты поиска не найдены"


