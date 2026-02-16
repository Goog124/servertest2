import sys
import requests
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

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

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key.Key_PageUp:
                tmp = int(self.lineEdit_delta.text())
                tmp = min(21, tmp + 1)
                self.lineEdit_delta.setText(str(tmp))
                self.run()

            if event.key() == Qt.Key.Key_PageDown:
                tmp = int(self.lineEdit_delta.text())
                tmp = max(1, tmp - 1)
                self.lineEdit_delta.setText(str(tmp))
                self.run()


            if event.key() == Qt.Key.Key_W:
                tmp = float(self.lineEdit_lat.text())
                z = int(self.lineEdit_delta.text())
                tmp += 10 / (z ** 3)
                self.lineEdit_lat.setText(str(tmp))
                self.run()

            if event.key() == Qt.Key.Key_A:
                tmp = float(self.lineEdit_lon.text())
                z = int(self.lineEdit_delta.text())
                tmp -= 10 / (z ** 3)
                self.lineEdit_lon.setText(str(tmp))
                self.run()

            if event.key() == Qt.Key.Key_S:
                tmp = float(self.lineEdit_lat.text())
                z = int(self.lineEdit_delta.text())
                tmp -= 10 / (z ** 3)
                self.lineEdit_lat.setText(str(tmp))
                self.run()

            if event.key() == Qt.Key.Key_D:
                tmp = float(self.lineEdit_lon.text())
                z = int(self.lineEdit_delta.text())
                tmp += 10 / (z ** 3)
                self.lineEdit_lon.setText(str(tmp))
                self.run()

        except Exception as E:
            self.statusBar().showMessage(E.__class__.__name__)
            return





def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())