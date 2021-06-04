try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui

except ImportError:
    raise ImportError("QT5 not founded")
from ..game_logic import *


class UIMenu(QWidget):
    def __init__(self, parent=None):
        super(UIMenu, self).__init__(parent)
        self.layout = QFormLayout()
        self.data = Data.get_instance()
        self.initUI()

    def initUI(self):
        self.start_btn = self.create_button("Start")
        self.credits_btn = self.create_button("Credits")
        self.exit_btn = self.create_button("Exit")

        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.credits_btn)
        self.layout.addWidget(self.exit_btn)
        self.setLayout(self.layout)

    def create_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("""*{margin: 6px;
        padding: 5px;
        border: 1px solid black;
        border-radius: 4px;
        background: #9BC4CB;
        color: #5F634F;
        }""" +
                          "*:hover {" +
                          "background: #5F634F;" +
                          "color: #9BC4CB;}")
        return btn
