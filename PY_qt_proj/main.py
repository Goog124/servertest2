import sys
import requests
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap

API_KEY = "5815d7d2-6bbe-424d-a32d-028b8c596fa2"


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('api_yand.ui', self)
        self.pushButton.clicked.connect(self.run)# Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        if not self.lineEdit_delta.text() or not self.lineEdit_lat.text() or not self.lineEdit_lon.text():
            self.statusBar().showMessage("Поля не заполнены")
            return
        else:
            self.statusBar().showMessage("")
            try:
                int(self.lineEdit_delta.text())
                float(self.lineEdit_lat.text())
                float(self.lineEdit_lon.text())
            except Exception as E:
                self.statusBar().showMessage("Некорректный ввод")
                return

        self.getImage()

    def getImage(self):
        api_server = 'https://static-maps.yandex.ru/v1?'
        # Готовим запрос.
        toponym_longitude = self.lineEdit_lon.text()
        toponym_lattitude = self.lineEdit_lat.text()
        z = int(self.lineEdit_delta.text())

        params = {
            "apikey": API_KEY,
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "z": z
        }

        response = requests.get(api_server, params=params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

        self.pixmap = QPixmap(self.map_file)
        self.map_picture.setPixmap(self.pixmap)




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())