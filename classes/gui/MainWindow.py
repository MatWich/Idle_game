try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
except ImportError:
    raise ImportError("QT5 not founded")
from .UIMenu import UIMenu
from .UIGame import UIGame
from settings import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Adventure Capitalist - Scaffed Edition")
        self.setWindowIcon(QIcon(ICON_IMG))
        self.menu()
        # self.game()

    def menu(self):
        """main menu"""
        self.setMinimumWidth(450)
        self.setMinimumHeight(350)
        self.UIMenu = UIMenu(self)
        self.UIMenu.start_btn.clicked.connect(self.game)
        self.setCentralWidget(self.UIMenu)
        self.show()

    def game(self):
        """initialize game screen"""
        self.setMinimumWidth(450)
        self.setMinimumHeight(350)
        self.UIGame = UIGame(self)
        self.setCentralWidget(self.UIGame)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(208, 240, 192, 255))
        painter.drawRect(0, 0, self.width(), self.height())