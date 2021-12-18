import sys
import copy

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.x = self.y = 0
        self.figura = 1
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Супрематизм')
        self.setMouseTracking(True)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        wh = randint(10, 300)
        if self.figura == 0:
            qp.drawEllipse(self.x, self.y, wh, wh)
        elif self.figura == 3:
            qp.drawPolygon([self.x, self.y - round(wh * 2/3)], [self.x + round(wh * 1/3), self.y + round(wh * 1/3)],
                           [self.x - round(wh * 2/3), self.y + round(wh * 1/3)])
        elif self.figura == 4:
            qp.drawRect(self.x - wh // 2, self.y - wh // 2, wh, wh)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.figura = 0
        elif (event.button() == Qt.RightButton):
            self.figura = 4

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.figura = 3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())