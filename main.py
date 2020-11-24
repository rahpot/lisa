import sys
import random as rd

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor, QBrush, QPen, QPixmap, QPainter


class YellowCycles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('UI')
        self.button.clicked.connect(self.draw)
        self.ok = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.ok != 0:
            self.drawCycles(qp)
        qp.end()

    def drawCycles(self, qp):
        for i in range(3):
            x = rd.randint(10, 800)
            y = rd.randint(10, 700)
            height = rd.randint(10, 257)
            qp.setBrush(QColor(255, 255, 0))
            qp.setPen(QColor(255, 255, 0))
            qp.drawEllipse(x, y, height, height)

    def draw(self):
        self.ok = 1
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = YellowCycles()
    widget.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
