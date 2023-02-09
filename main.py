import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

from get_image import getImage

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.scale = 15
        self.initUI()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_PageUp:
            self.scale -= 1
            self.show_image()
        elif event.key() == Qt.Key_PageDown:
            self.scale += 1
            self.show_image()
        if event.key() == Qt.Key_Up:
            coord1, coord2 = self.coordinates.split(',')
            coord1, coord2 = float(coord1), float(coord2)
            self.coordinates = str(coord1) + ',' + str(coord2 + 800 / (2 ** self.scale))
            self.show_image()
        if event.key() == Qt.Key_Down:
            coord1, coord2 = self.coordinates.split(',')
            coord1, coord2 = float(coord1), float(coord2)
            self.coordinates = str(coord1) + ',' + str(coord2 - 800 / (2 ** self.scale))
            self.show_image()
        if event.key() == Qt.Key_Left:
            coord1, coord2 = self.coordinates.split(',')
            coord1, coord2 = float(coord1), float(coord2)
            self.coordinates = str(coord1 - 512 / (2 ** self.scale)) + ',' + str(coord2)
            self.show_image()
        if event.key() == Qt.Key_Right:
            coord1, coord2 = self.coordinates.split(',')
            coord1, coord2 = float(coord1), float(coord2)
            self.coordinates = str(coord1 + 512 / (2 ** self.scale)) + ',' + str(coord2)
            self.show_image()

    def show_image(self):
        getImage(self.scale, self.coordinates)
        self.map_file = 'map.png'
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.coordinates = '37.530887,55.70311'
        self.setWindowTitle('Отображение карты')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.show_image()

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
