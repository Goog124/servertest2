import requests


def find_spn(toponim_name):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "73ea1519-8fff-4060-b918-768a12d35d45",
        "geocode": toponim_name,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_size = toponym["boundedBy"]["Envelope"]
    x1, y1 = toponym_size["lowerCorner"].split()
    x2, y2 = toponym_size["upperCorner"].split()
    toponym_size = (float(x2) - float(x1), float(y2) - float(y1))

    return toponym_size