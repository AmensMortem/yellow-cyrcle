import random
import sys

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_UI import Ui_MainWindow


class Paint_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw_btn.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(1, min([self.width(), self.height()]))
        x = random.randint(0, self.width() - diameter - 1)
        y = random.randint(0, self.height() - diameter - 1)
        color = [random.randint(0, 255) for _ in range(3)]
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
