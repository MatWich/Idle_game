try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui

except ImportError:
    raise ImportError("QT5 not founded")

import threading
import time

from ..game_logic import *


class UIGame(QWidget):
    def __init__(self, parent=None):
        super(UIGame, self).__init__(parent)
        self.incs = []
        self.layout = QGridLayout()
        self.leftVBox = QVBoxLayout()
        self.rightVBox = QVBoxLayout()
        self.data = Data.get_instance()
        self.initUI()

    def initUI(self):
        self.layout.addLayout(self.leftVBox, 0, 0)
        self.layout.addLayout(self.rightVBox, 0, 1)
        self.setLayout(self.layout)


