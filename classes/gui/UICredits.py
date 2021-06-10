try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtCore import QThread, pyqtSignal, QTimer

except ImportError:
    raise ImportError("QT5 not founded")

from ..game_logic import Data


class UICredits(QWidget):
    def __init__(self, parent=None):
        super(UICredits, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.data = Data.get_instance()
        self.initFonts()
        self.initUI()

    def initUI(self):
        self.title_lbl = QLabel()
        self.title_lbl.setText("Credits")
        self.title_lbl.setFont(self.title_font)
        self.title_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.content_lbl = QLabel()
        self.content_lbl.setText("Well I have no idea what should I put this XD")
        self.content_lbl.setFont(self.content_font)
        self.content_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.back_btn = QPushButton("back")
        self.back_btn.setStyleSheet("""*{margin: 6px;
               padding: 5px;
               border: 1px solid black;
               border-radius: 4px;
               background: #9BC4CB;
               color: #5F634F;
               }""" +
                          "*:hover {" +
                          "background: #5F634F;" +
                          "color: #9BC4CB;}")

        self.layout.addWidget(self.title_lbl)
        self.layout.addWidget(self.content_lbl)
        self.layout.addWidget(self.back_btn)

        self.setLayout(self.layout)

    def initFonts(self):
        self.title_font = QFont("Trajan Pro", 20, 700)
        self.content_font = QFont("Trajan Pro", 10, 700)
