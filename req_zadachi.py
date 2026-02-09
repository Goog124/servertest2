import requests
import json

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'
geocode = 'Музей'
# Готовим запрос.
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    json_response = response.json()
    # Запрос успешно выполнен, печатаем полученные данные.
    with open("mus.json", mode="w", encoding="utf8") as f:
        json.dump(response.json(), f, ensure_ascii=False)

    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"]['AdministrativeAreaName']
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_address, "имеет координаты:", toponym_coodrinates)
else:
    # Произошла ошибка выполнения запроса. Обрабатываем http-статус.
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")