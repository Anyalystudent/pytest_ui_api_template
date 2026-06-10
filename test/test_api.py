import requests
import pytest

from Pages.MainPage import MainPage

def test_search_product(driver):
    main_page = MainPage(driver)

    title = "чиабатта"
    result = main_page.search(title)

    assert result.status_code == 200
    assert len(result) > 0