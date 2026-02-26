import requests



API_KEY = "d22c94bf-f47a-4b5d-abd6-6e428312d7c8"


def get_station_code(a, b, time):
    url = (f'https://api.rasp.yandex.net/v3.0/search/?apikey={API_KEY}&from={a}&to={b}&'
           f'format=json&lang=ru_RU&date={time}&transport_types=train')
    response = requests.get(url)
    data = response.json()

    try:
        res = set()
        for i in data["segments"]:
            res.add(i["thread"]["title"])
        print(*sorted(res), sep="\n")
    except (KeyError, IndexError):
        print("Что-то пошло не так, возможно, индексы сдвинулись. Жизнь — боль.")


a, b = input().split()
time = input()
get_station_code(a, b, time)
