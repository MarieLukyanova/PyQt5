import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 500, 600)
        self.setWindowTitle('Рисунок')
        self.btn = QPushButton('Показать', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.draw)
        self.lbl1 = QLabel('side', self)
        self.lbl1.move(120, 10)
        self.side = QLineEdit(self)
        self.side.move(150, 10)
        self.lbl2 = QLabel('coeff', self)
        self.lbl2.move(120, 50)
        self.coeff = QLineEdit(self)
        self.coeff.move(150, 50)
        self.lbl3 = QLabel('n', self)
        self.lbl3.move(120, 90)
        self.kolvo = QLineEdit(self)
        self.kolvo.move(150, 90)
        self.n = 0
        self.k = 0
        self.weight = 0

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_rect(qp)
            qp.end()

    def draw_rect(self, qp):
        try:
            self.n = int(self.kolvo.text())
            self.k = float(self.coeff.text())
            self.weight = int(self.side.text())
            if self.n <= 0:
                raise ValueError
            side = self.weight
            if side <= 0:
                raise ValueError
            c = self.k
            if not 0 <= c <= 1:
                raise ValueError
            x, y = self.width() // 2,  self.height() // 2
            qp.setPen(QColor('red'))
            qp.setBrush(Qt.NoBrush)
            for _ in range(self.n):
                qp.drawRect(x - side // 2, y - side // 2, side, side)
                side = int(side * c)
        except ValueError:
            pass

    def draw(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())