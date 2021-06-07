import threading
import time

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtCore import QThread, pyqtSignal

except ImportError:
    raise ImportError("QT5 not founded")

from ..game_logic import *


class PrThread(QThread):
    change_value = pyqtSignal(int)

    def __init__(self, parent=None, inc=None, index=0):
        super(PrThread, self).__init__(parent)
        self.inc = inc
        self.index = index
        self.is_running = True
        self.data = Data.get_instance()

    def run(self):
        cnt = 0
        print(f"Starting... {self.index}")
        while cnt < 100:
            if cnt == 99:
                cnt = 0
                self.data.profit += self.inc.profit
            cnt += 1
            time.sleep(0.01)
            self.change_value.emit(cnt)

    def stop(self):
        self.is_running = False
        print(f"SPOPPED {self.inc} ")
        self.terminate()


class UIGame(QWidget):
    def __init__(self, parent=None):
        super(UIGame, self).__init__(parent)
        self.incs = []
        self.layout = QGridLayout()
        self.leftVBox = QVBoxLayout()
        self.rightVBox = QVBoxLayout()
        self.data = Data.get_instance()
        self.threads = {}
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

        self.data.lemonShop_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.lemonShop_inc))
        self.data.paper_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.paper_inc))
        self.data.car_wash_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.car_wash_inc))
        self.data.pizza_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.pizza_inc))
        self.data.donut_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.donut_inc))

        self.data.sea_food_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.sea_food_inc))
        self.data.hokey_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.hokey_inc))
        self.data.camera_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.camera_inc))
        self.data.white_house_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.white_house_inc))
        self.data.oil_inc.upgrade_btn.clicked.connect(lambda: self.startProgressBar(self.data.oil_inc))


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
        inc.image_lbl.setPixmap(QPixmap(inc.image).scaled(64, 64))
        inc.upgrade_btn = QPushButton(f"Upgrade for: {inc.upgrade_cost}")
        inc.upgrades_no_lbl = QLabel()
        inc.upgrades_no_lbl.setNum(inc.upgrades_no)

        inc.layout = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(inc.upgrade_btn)
        hbox.addWidget(inc.upgrades_no_lbl)

        inc.layout.addWidget(inc.image_lbl)
        vbox.addWidget(inc.pr_bar)
        vbox.addLayout(hbox)

        inc.layout.addLayout(vbox)

        # inc.layout = QGridLayout()
        # vbox1 = QVBoxLayout()
        # vbox2 = QVBoxLayout()
        # hbox = QHBoxLayout()
        #
        # hbox.addWidget(inc.upgrade_btn)
        # hbox.addWidget(inc.upgrades_no_lbl)
        # vbox1.addWidget(inc.image_lbl)
        #
        # vbox2.addWidget(inc.pr_bar)
        # vbox2.addLayout(hbox)
        #
        # inc.layout.addLayout(vbox1, 0, 0, 2, 2)
        # inc.layout.addLayout(vbox2, 0, 2, 1, 1)

    def startProgressBar(self, inc):
        print(f'inc index: {inc.index}')
        self.threads[inc.index] = PrThread(inc=inc, index=inc.index)
        self.threads[inc.index].change_value.connect(self.setProgressValue)
        self.threads[inc.index].start()

    def setProgressValue(self, val):
        index = self.sender().index
        print(index)

        self.data.incs[index - 1].pr_bar.setValue(val)
