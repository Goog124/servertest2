import os
import sys
import requests
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "MAP"
MAP_FILE = "map.png"


class GameView(arcade.Window):
    def setup(self):
        self.get_image()

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(
                (self.width - self.background.width) // 2,
                (self.height - self.background.height) // 2,
                self.background.width,
                self.background.height
            ),
        )

    def get_image(self):

        api_server = "https://static-maps.yandex.ru/v1"

        geocode = "Великий Новгород"
        apikey_static = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        apikey_geo = "8013b162-6b42-4997-9691-77b7074026e0"

        geo = f"https://geocode-maps.yandex.ru/v1/?apikey={apikey_geo}&geocode=Австралия&format=json"
        response = requests.get(geo)
        if response:
            json_response = response.json()
            ll = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            print(ll)

            params = {
                "ll": ll.replace(" ", ","),
                "z": "4",
                "size": ",".join([str(650), str(450)]),
                "apikey": apikey_static,
            }
            response = requests.get(api_server, params=params)
            print(response.url)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        with open(MAP_FILE, "wb") as file:
            file.write(response.content)

        self.background = arcade.load_texture(MAP_FILE)


def main():
    gameview = GameView(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    gameview.setup()
    arcade.run()
    # Удаляем за собой файл с изображением.
    os.remove(MAP_FILE)


if __name__ == "__main__":
    main()