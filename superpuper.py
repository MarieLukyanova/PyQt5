import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
from random import randint


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


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
            qp.drawEllipse(self.x - wh // 2, self.y - wh // 2, wh, wh)
        elif self.figura == 3:
            qp.drawPolygon(QPoint(self.x, self.y - int(wh * 3 ** 0.5 / 4)),
                           QPoint(self.x + wh // 2, self.y +
                                  int(wh * 3 ** 0.5 / 4)),
                           QPoint(self.x - wh // 2, self.y + int(
                               wh * 3 ** 0.5 / 4))
                           )
        elif self.figura == 4:
            qp.drawRect(self.x - wh // 2, self.y - wh // 2, wh, wh)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.figura = 0
        elif event.button() == Qt.RightButton:
            self.figura = 4
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.figura = 3
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())