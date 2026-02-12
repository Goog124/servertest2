import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "73ea1519-8fff-4060-b918-768a12d35d45",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)


if not response:
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
toponym_size = toponym["boundedBy"]["Envelope"]
x1, y1 = toponym_size["lowerCorner"].split()
x2, y2 = toponym_size["upperCorner"].split()
print(x1, y1)
print(x2, y2)
toponym_size = (abs(float(x2) - float(x1)), abs(float(y2) - float(y1)))

print(toponym_size)
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

apikey = "5815d7d2-6bbe-424d-a32d-028b8c596fa2"
# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([str(toponym_size[0]), str(toponym_size[1])]),
    "apikey": apikey,
    "pt": f"{toponym_longitude},{toponym_lattitude},pmvvl"
}

map_api_server = "https://static-maps.yandex.ru/v1"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
im = BytesIO(response.content)
opened_image = Image.open(im)
opened_image.show()  # Создадим картинку и тут же ее покажем встроенным просмотрщиком операционной системы
