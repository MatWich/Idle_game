try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
except ImportError:
    raise ImportError("QT5 not founded")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def menu(self):
        """main menu"""
        pass

    def game(self):
        """initialize game screen"""
        pass
