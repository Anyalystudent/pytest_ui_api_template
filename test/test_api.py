import requests
import pytest
import allure
from cookies import COOKIES

URL = "https://market-delivery.yandex.ru"
my_headers = {
    "Cookie": COOKIES,
    "Cache-Control": "no-cache",
    "x-platform": "dc_desktop_web",
    "Content-Type": "application/json",
}
my_params = {
    "soft_multi": "true",
    "longitude": 37.59217698696895,
    "latitude": 55.750078863243985,
    "screen": "search",
    "shippingType": "delivery",
    "autoTranslate": "false",
    "plus_subscription_toggle_state": "false",
    "placeSlug": "perekrestok_spgoy",
}


@allure.story("Поиск товара")
@allure.feature("READ")
@allure.title("Поиск товара через строку поиска")
def test_search_product():
    """
    тест на поиск товара
    """
    title = "чиабатта"
    body = {
        "text": title,
        "filters": [],
        "location": {"longitude": 37.59217698696895, "latitude": 55.750078863243985},
    }
    result = requests.post(url=f"{URL}/eats/v1/full-text-search/v1/search", json=body)
    with allure.step("Проверить статус-код ответа = 200"):
        assert result.status_code == 200
    with allure.step("Проверить, что ответ не пустой"):
        response_body = result.json()
        assert response_body is not None


@allure.story("Добавление товара")
@allure.feature("CREATE")
@allure.title("Добавление и удаление товара")
def test_add_and_delete_product():
    """
    тест на добавление и удаление товара
    """
    body = {
        "quantity": 1,
        "place_slug": "perekrestok_spgoy",
        "place_business": "shop",
        "item_id": "5ceac0d8-9085-4b2e-a531-ca437749dcc1",
    }
    result = requests.post(
        url=f"{URL}/api/v1/cart", params=my_params, headers=my_headers, json=body
    )
    with allure.step("Проверить статус-код ответа = 200"):
        assert result.status_code == 200
    with allure.step("Взять из тела ответа значение ключа id, и записать в переменную"):
        response_body = result.json()
        id = response_body["id"]
    with allure.step(f"Удалить добавленный в корзину товар со значением {id}"):
        delete_result = requests.delete(
            url=f"{URL}/api/v1/cart/{id}", params=my_params, headers=my_headers
        )
    with allure.step("Проверить статус-код ответа = 200"):
        assert delete_result.status_code == 200


@allure.story("Изменение количества товара")
@allure.feature("UPDATE")
@allure.title("Добавление, изменение количества и удаление товара")
def test_add_and_edite_product():
    """
    Тест на добавление и изменение количества продукта
    """
    body = {
        "quantity": 1,
        "place_slug": "perekrestok_spgoy",
        "place_business": "shop",
        "item_id": "5ceac0d8-9085-4b2e-a531-ca437749dcc1",
    }
    result = requests.post(
        url=f"{URL}/api/v1/cart", params=my_params, headers=my_headers, json=body
    )
    with allure.step("Проверить статус-код ответа = 200"):
        assert result.status_code == 200
    with allure.step("Взять из тела ответа значение ключа id, и записать в переменную"):
        response_body = result.json()
        id = response_body["id"]

    edite_body = {"quantity": 2, "item_options": []}
    with allure.step("Изменить количество товара"):
        edite_result = requests.put(
            url=f"{URL}/api/v1/cart/{id}",
            params=my_params,
            headers=my_headers,
            json=edite_body,
        )
    with allure.step("Проверить статус-код ответа = 200"):
        assert edite_result.status_code == 200
    with allure.step("Проверить, что количество изменилось и равно 2"):
        assert edite_result.json()["cart"]["items"][0]["quantity"] == 2
    with allure.step("Проверить, что id товара не поменялся"):
        assert edite_result.json()["cart"]["items"][0]["id"] == id

    # удаляем добавленный в корзину товар
    with allure.step(f"Удалить добавленный в корзину товар со значением {id}"):
        delete_result = requests.delete(
            url=f"{URL}/api/v1/cart/{id}", params=my_params, headers=my_headers
        )
    with allure.step("Проверить статус-код ответа = 200"):
        assert delete_result.status_code == 200


@allure.story("Поиск товара")
@allure.feature("READ")
@allure.title("Поиск несуществующего товара через строку поиска")
def test_search_negative():
    """
    тест на поиск несуществующего товара
    """
    title = "прткгвд"
    body = {
        "text": title,
        "filters": [],
        "location": {"longitude": 37.59217698696895, "latitude": 55.750078863243985},
    }
    result = requests.post(url=f"{URL}/eats/v1/full-text-search/v1/search", json=body)
    with allure.step("Проверить статус-код ответа = 200"):
        assert result.status_code == 200
    with allure.step("Проверить, что в ответе текст 'Ничего не нашли, но есть:'"):
        response_body = result.json()
        expected_text = "Ничего не нашли, но есть:"
        assert expected_text in response_body["header"]["text"]


@allure.story("Добавление товара")
@allure.feature("CREATE")
@allure.title("Добавление товара с неверным методом запроса")
def test_add_product_negative():
    """
    Тест на добавление продукта с неверным методом запроса
    """
    body = {
        "quantity": 1,
        "place_slug": "pyatyorochka_9k6zf",
        "place_business": "shop",
        "item_id": "7f65eb1c-b600-4e6a-8f79-3b334f4eed37",
    }
    result = requests.get(
        url=f"{URL}/api/v1/cart", params=my_params, headers=my_headers, json=body
    )
    with allure.step("Проверить статус-код ответа = 400"):
        assert result.status_code == 400
    response_body = result.json()
    with allure.step("Проверить значение 'code' в ответе"):
        assert response_body["code"] == "get_head_cannot_have_body"
    # проверка текста сообщения
    with allure.step("Проверить значение 'message' в ответе"):
        assert response_body["message"] == "Request cannot have content"
