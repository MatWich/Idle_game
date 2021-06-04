try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
except ImportError:
    raise ImportError("QT5 not founded")
from .UIMenu import UIMenu


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.menu()

    def menu(self):
        """main menu"""
        self.setMinimumWidth(450)
        self.setMinimumHeight(350)
        self.UIMenu = UIMenu(self)
        self.setCentralWidget(self.UIMenu)
        self.show()

    def game(self):
        """initialize game screen"""
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(208, 240, 192, 255))
        painter.drawRect(0, 0, self.width(), self.height())