import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QErrorMessage


class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 500, 600)
        self.setWindowTitle('Рисунок')
        self.btn = QPushButton('Показать', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.f)
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
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        x, y = 240 - (self.weight // 2), 350 - (self.weight // 2)
        qp.setBrush(QColor(255, 0, 0))
        for _ in range(self.n):
            qp.drawRect(x, y, self.weight, self.weight)
            self.weight = round(self.k * self.weight)
            x = 240 - (self.weight // 2)
            y = x + 110

    def f(self):
        self.n = int(self.kolvo.text())
        self.k = float(self.coeff.text())
        self.weight = int(self.side.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())