import requests


API_KEY = "19dfc3dc-cc95-4a48-a9d2-be00f96ff93d"

headers = {
    "X-Yandex-Weather-Key": API_KEY
}

lat, lon, delta = input().split()

query1 = f"""{{
  weatherByPoint(request: {{ lat: {lat}, lon: {lon} }}) {{
    now {{
      temperature
      humidity
      pressure
      windSpeed
      windDirection
    }}
  }}
}}"""

lon = float(lon) + float(delta)
query2 = f"""{{
  weatherByPoint(request: {{ lat: {lat}, lon: {lon} }}) {{
    now {{
      temperature
      humidity
      pressure
      windSpeed
      windDirection
    }}
  }}
}}"""

# Отправляем POST-запрос
# Важно: GraphQL почти всегда живёт на POST-запросах, потому что мы передаём тело
response1 = requests.post(
    'https://api.weather.yandex.ru/graphql/query',
    headers=headers,
    json={'query': query1}
)

response2 = requests.post(
    'https://api.weather.yandex.ru/graphql/query',
    headers=headers,
    json={'query': query2}
)

# Проверяем, был ли сервер к нам благосклонен (код 200 — всё ок)
if response1.status_code == 200 and response2.status_code == 200:
    data1 = response1.json()
    data2 = response2.json()
    # Раскапываем JSON, как археологи
    temp1 = data1['data']['weatherByPoint']['now']
    temp2 = data2['data']['weatherByPoint']['now']
    for key, value1, value2 in zip(temp1.keys(), temp1.values(), temp2.values()):
        print(key, value1, value2, sep="\t")

    # Для любопытных: выведем всё мясо ответа
    # print(json.dumps(data, indent=2, ensure_ascii=False))
else:
    print("🔥 Хьюстон, у нас проблема:", response1.status_code)
    print(response1.text)