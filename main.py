import sys
import random as rd

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor, QBrush, QPen, QPixmap, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(270, 220, 251, 171))
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "dont push me"))



class YellowCycles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.draw)
        self.ok = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.ok != 0:
            self.drawCycles(qp)
        qp.end()

    def drawCycles(self, qp):
        for i in range(200):
            r = rd.randint(0, 255)
            g = rd.randint(0, 255)
            b = rd.randint(0, 255)
            x = rd.randint(0, 800)
            y = rd.randint(0, 700)
            height = rd.randint(10, 257)
            qp.setBrush(QColor(r, g, b))
            qp.setPen(QColor(r, g, b))
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
