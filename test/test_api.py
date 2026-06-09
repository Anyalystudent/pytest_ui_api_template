
from Pages.MainPage import MainPage

def test_search_product(driver):
    main_page = MainPage(driver)
    main_page.search("чиабатта")


