import random
import sys
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Paint_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.draw_btn.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(1, min([self.width(), self.height()]))
        x = random.randint(0, self.width() - diameter - 1)
        y = random.randint(0, self.height() - diameter - 1)
        color = (255, 242, 000)
        self.circles += [(color, (x, y, diameter, diameter))]
        self.update()

    def draw(self, pan):
        pan.setBrush(QColor(0, 0, 0, 0))
        for color, data in self.circles:
            pen = QPen(QColor(*color), 5)
            pan.setPen(pen)
            pan.drawEllipse(*data)

    def paintEvent(self, *args, **kwargs):
        pan = QPainter()
        pan.begin(self)
        self.draw_circles(pan)
        pan.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Paint_Window()
    window.show()
    sys.exit(app.exec())
