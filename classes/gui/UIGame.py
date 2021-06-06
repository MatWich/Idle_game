try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui

except ImportError:
    raise ImportError("QT5 not founded")

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
        self.create_company(self.data.lemonShop_inc)
        self.create_company(self.data.paper_inc)
        self.create_company(self.data.car_wash_inc)
        self.create_company(self.data.pizza_inc)
        self.create_company(self.data.donut_inc)
        self.create_company(self.data.sea_food_inc)
        self.create_company(self.data.hokey_inc)
        self.create_company(self.data.camera_inc)
        self.create_company(self.data.white_house_inc)
        self.create_company(self.data.oil_inc)

        """ Left layout """

        self.leftVBox.addLayout(self.data.lemonShop_inc.layout)
        self.leftVBox.addLayout(self.data.paper_inc.layout)
        self.leftVBox.addLayout(self.data.car_wash_inc.layout)
        self.leftVBox.addLayout(self.data.pizza_inc.layout)
        self.leftVBox.addLayout(self.data.donut_inc.layout)

        """ Right layout """

        self.rightVBox.addLayout(self.data.sea_food_inc.layout)
        self.rightVBox.addLayout(self.data.hokey_inc.layout)
        self.rightVBox.addLayout(self.data.camera_inc.layout)
        self.rightVBox.addLayout(self.data.white_house_inc.layout)
        self.rightVBox.addLayout(self.data.oil_inc.layout)

        self.layout.addLayout(self.leftVBox, 0, 0)
        self.layout.addLayout(self.rightVBox, 0, 1)
        self.setLayout(self.layout)

    def create_company(self, inc):
        """ You have to provide an Inc object"""
        inc.pr_bar = QProgressBar()
        inc.image_lbl = QLabel()
        inc.image_lbl.setPixmap(QPixmap(inc.image).scaled(32, 32))
        inc.upgrade_btn = QPushButton(f"Upgrade for: {inc.upgrade_cost}")
        inc.upgrades_no_lbl = QLabel()
        inc.upgrades_no_lbl.setNum(inc.upgrades_no)
        inc.layout = QGridLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(inc.upgrade_btn)
        hbox.addWidget(inc.upgrades_no_lbl)
        vbox1.addWidget(inc.image_lbl)

        vbox2.addWidget(inc.pr_bar)
        vbox2.addLayout(hbox)

        inc.layout.addLayout(vbox1, 0, 0, 2, 2)
        inc.layout.addLayout(vbox2, 0, 3, 1, 1)
