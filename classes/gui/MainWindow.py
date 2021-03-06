try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
except ImportError:
    raise ImportError("QT5 not founded")
from .UIMenu import UIMenu
from .UIGame import UIGame
from .UICredits import UICredits
from settings import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Adventure Capitalist - Scaffed Edition")
        self.setWindowIcon(QIcon(ICON_IMG))
        self.setMinimumWidth(500)
        self.setMinimumHeight(550)
        self.menu()
        # self.game()

    def menu(self):
        """main menu"""
        self.UIMenu = UIMenu(self)
        self.UIMenu.start_btn.clicked.connect(self.game)
        self.UIMenu.credits_btn.clicked.connect(self.credits)
        self.UIMenu.exit_btn.clicked.connect(self.exit)
        self.setCentralWidget(self.UIMenu)
        self.show()

    def game(self):
        """initialize game screen"""
        self.UIGame = UIGame(self)
        self.setCentralWidget(self.UIGame)
        self.show()

    def credits(self):
        """initialize credits"""
        self.setMinimumWidth(450)
        self.setMinimumHeight(350)
        self.UICredits = UICredits(self)
        self.UICredits.back_btn.clicked.connect(self.menu)
        self.setCentralWidget(self.UICredits)
        self.show()

    def exit(self):
        QApplication.quit()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(208, 240, 192, 255))
        painter.drawRect(0, 0, self.width(), self.height())