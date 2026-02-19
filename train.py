import requests

API_KEY = "d22c94bf-f47a-4b5d-abd6-6e428312d7c8"


# Шаг 1. Ищем код станции (теоретически это делается один раз)
# Но мы же учимся, давайте глянем, как найти код Москвы (c213) в этой куче данных
# ВНИМАНИЕ: этот запрос тяжёлый, лучше сохранить результат в файлик

def get_station_code(a, b, time):
    url = (f'https://api.rasp.yandex.net/v3.0/search/?apikey={API_KEY}&from={a}&to={b}&'
           f'format=json&lang=ru_RU&date={time}&transport_types=train')
    response = requests.get(url)
    data = response.json()

    # Путь ниндзя к коду Москвы через дебри JSON:
    # Страны -> Россия (29) -> Регионы -> Москва (37) -> Населённые пункты -> Москва (316)
    # P. S. Индексы могут меняться, в реальном коде так жёстко их не зашивают, но для примера сойдёт
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
