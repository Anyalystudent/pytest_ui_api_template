import requests
import pytest

from Pages.MainPage import MainPage

URL = 'https://market-delivery.yandex.ru'
my_headers = {
        'Cookie': 'is_gdpr=0; is_gdpr_b=CL/mIhCa1AIoAg==; yandexuid=3874611751756366349; yashr=5647430301756366349; yuidss=3874611751756366349; ymex=2071726352.yrts.1756366352; _ym_uid=1756366353738063242; _ym_d=1756366361; my=YwA=; gdpr=0; amcuid=1655385451757856147; i=7nvzdtjHm43WXojx6QUHmWdqWur+g0mQ4og89445JaGwBNq3XEqho5Sme0YvP6ByFxuWTxQbPoMibJM7vLITXpch3og=; Eats-Session=32eb9751609e489bb6b39c9678bce133; L=V3l5dkZeS210V3BvdwV8AVIPZEFlQEh2KDs9LDoJ.1771775356.1729960.357935.6a205065edebd860750be8653cfe8ce3; cycada=Q1uaEZkIRODJ7WSOXxfxYRhg19Hhv8VR8O0p8zfgO4Q=; isa=8xulgypdOqTZqDMj3FgRWB+jwr0GqMOPoQj8/r7O1AtiekTW5K7IR5eaHnFCieOxZy8Ol+3KFRGXr1R6dVVKqH1iMlU=; sae=0:04704849-6CC0-4DDF-9029-60A16DE6171D:p:25.12.4.1216:w:d:RU:20250828; _ym_isad=2; eda_web_adult_age=0; yandex_login=; ys=c_chck.3640558059; _yasc=elyLl8sdxoTswj/X/SpskbEyDftazzisEn0LTdbjAelx40uC/jk0daj//HcH7N5JzDNSPysoOx8u2lmwPp6Y; bh=ElEiQ2hyb21pdW0iO3Y9IjE0MiIsICJZYUJyb3dzZXIiO3Y9IjI1LjEyIiwgIk5vdF9BIEJyYW5kIjt2PSI5OSIsICJZb3dzZXIiO3Y9IjIuNSIaBSJ4ODYiIgwyNS4xMi40LjEyMTYqAj8wMgIiIjoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJqIkNocm9taXVtIjt2PSIxNDIuMC43NDQ0LjEyMTYiLCAiWWFCcm93c2VyIjt2PSIyNS4xMi40LjEyMTYiLCAiTm90X0EgQnJhbmQiO3Y9Ijk5LjAuMC4wIiwgIllvd3NlciI7dj0iMi41IloCPzBgobv3zAZqIdzK4f8IktihsQOfz+HqA/v68OcN6//99g/4nPzXAvOBAg==; yp=1772037705.uc.ru#1772037705.duc.ru#1771960905.gpauto.61_088997:43_163898:100000:3:1771953705#1789392104.cld.2261448#1787543367.szm.1:1280x1024:1265x880#2086712569.pcs.0#1802888569.swntab.0#1797442469.dc_neuro.6#1789392104.brd.6301000000#1774030971.hdrc.1#2086621763.multib.1#1772216569.dlp.1; gpauto=61_088997:43_163898:100000:3:1771953705; eda_web={%22app%22:{%22analyticsSession%22:{%22id%22:%22mm0vedgc-vtw2z9vax8j-x5m5u356z4g-2gb73toa98g%22%2C%22start%22:1771953529%2C%22update%22:1771953722}%2C%22deliveryTime%22:null%2C%22themeVariantKey%22:%22light%22%2C%22xDeviceId%22:%22mlpf14kb-lec3p7ov9o-3xvmdy9uqms-0vy806h5oqx9%22%2C%22lastObtainedGps%22:{%22lat%22:61.08899688720703%2C%22lon%22:43.16389846801758%2C%22timestamp%22:1771953724916}%2C%22lat%22:55.750078863243985%2C%22lon%22:37.59217698696895}}',
        'Cache-Control': 'no-cache',
        'Postman-Token': '<calculated when request is sent>',
        'x-platform': 'dc_desktop_web',
        'Content-Type': 'application/json'
}
my_params = {
        'soft_multi': 'true',
        'longitude': 37.59217698696895,
        'latitude': 55.750078863243985,
        'screen': 'search',
        'shippingType': 'delivery',
        'autoTranslate': 'false',
        'plus_subscription_toggle_state': 'false',
        'placeSlug': 'perekrestok_spgoy'
    }

def test_search_product():
    '''
    тест на поиск товара
    '''
    title = "чиабатта"
    body = {"text": "чиабатта",
    "filters": [],
    "location": {
        "longitude": 37.59217698696895,
        "latitude": 55.750078863243985
        }
    }
    result = requests.post(url= f'{URL}/eats/v1/full-text-search/v1/search', json=body)

    assert result.status_code == 200
    # проверяем, что ответ не пустой
    response_body = result.json()
    assert response_body is not None


def test_add_and_delete_product():
    '''
    тест на добавление и удаление товара
    '''
    body = {
    "quantity": 1,
    "place_slug": "perekrestok_spgoy",
    "place_business": "shop",
    "item_id": "5ceac0d8-9085-4b2e-a531-ca437749dcc1"
    }
    result = requests.post(url=f'{URL}/api/v1/cart?soft_multi=true&longitude=37.59217698696895&latitude=55.750078863243985', json=body)
    assert result.status_code == 200
    response_body = result.json()
    id = response_body['id']
    #удаляем добавленный в корзину товар
    delete_result = requests.delete(url=f'{URL}/api/v1/cart/{id}', params=my_params, headers=my_headers)
    assert delete_result.status_code == 200

def test_add_and_edite_product():
    '''
    Тест на добавление и изменение количества продукта
    '''
    body = {
    "quantity": 1,
    "place_slug": "perekrestok_spgoy",
    "place_business": "shop",
    "item_id": "5ceac0d8-9085-4b2e-a531-ca437749dcc1"
    }
    result = requests.post(url=f'{URL}/api/v1/cart?soft_multi=true&longitude=37.59217698696895&latitude=55.750078863243985', json=body)
    assert result.status_code == 200
    response_body = result.json()
    id = response_body['id']

    # изменяем количество товара
    edite_body = {
        "quantity": 2,
        "item_options": []
    }
    edite_result = requests.put(url=f'{URL}/api/v1/cart/{id}', params=my_params, headers=my_headers, json=edite_body)
    assert edite_result.status_code == 200
    # проверяем, что количество равно 2
    assert edite_result.json()['quantity'] == 2
    # проверяем, что id не поменялся
    assert edite_result.json()['id'] == id

    #удаляем добавленный в корзину товар
    delete_result = requests.delete(url=f'{URL}/api/v1/cart/{id}', params=my_params, headers=my_headers)
    assert delete_result.status_code == 200

def test_search_negative():
    '''
    тест на поиск несуществующего товара
    '''
    title = "прткгвд"
    body = {"text": "прткгвд",
    "filters": [],
    "location": {
        "longitude": 37.59217698696895,
        "latitude": 55.750078863243985
        }
    }
    result = requests.post(url= f'{URL}/eats/v1/full-text-search/v1/search', json=body)
    assert result.status_code == 200
    # проверяем, в ответе текст "Ничего не нашли, но есть:"
    response_body = result.json()
    expected_text = "Ничего не нашли, но есть:"
    assert expected_text in response_body['header']['text']

def test_add_product_negative():
    '''
    Тест на добавление продукта с неверным методом запроса
    '''
    body = {
        "quantity": 1,
        "place_slug": "pyatyorochka_9k6zf",
        "place_business": "shop",
        "item_id": "7f65eb1c-b600-4e6a-8f79-3b334f4eed37"
    }
    result = requests.get(
        url=f'{URL}/api/v1/cart?soft_multi=true&longitude=37.59217698696895&latitude=55.750078863243985', json=body)
    assert result.status_code == 400
    response_body = result.json()
    # проверка кода ошибки
    assert response_body['code'] == "get_head_cannot_have_body"
    # проверка текста сообщения
    assert response_body['message'] == "Request cannot have content"