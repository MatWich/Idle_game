import threading
import time

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtCore import QThread, pyqtSignal, QTimer

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
                self.data.money += self.inc.profit + self.inc.profit * self.inc.upgrades_no
            cnt += 1
            time.sleep(self.inc.time)
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
        self.topLayout = QHBoxLayout()
        self.leftVBox = QVBoxLayout()
        self.rightVBox = QVBoxLayout()
        self.data = Data.get_instance()
        self.threads = {}
        self.initUI()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(lambda: self.update_labels())
        self.timer.start()

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

        """ BUTTONS """

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

        """ TOP Layout """
        self.adv_cap_font_big = QFont("Trajan Pro", 20, 700)
        self.money_label = QLabel()
        self.money_label.setText(f"Money: {self.data.money}")
        self.money_label.setFont(self.adv_cap_font_big)
        self.btn = QPushButton(f"Make 1 $")
        self.btn.setFont(self.adv_cap_font_big)
        self.btn.clicked.connect(self.increase_money)

        self.topLayout.addWidget(self.money_label)
        self.topLayout.addWidget(self.btn)



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

        self.layout.addLayout(self.topLayout, 0, 0, 2, 2)
        self.layout.addLayout(self.leftVBox, 2, 0, 1, 1)
        self.layout.addLayout(self.rightVBox, 2, 1, 1, 1)
        self.setLayout(self.layout)

    def create_company(self, inc):
        """ You have to provide an Inc object"""
        self.adv_cap_font_small = QFont("Trajan Pro", 10, 700)
        inc.pr_bar = QProgressBar()
        inc.image_lbl = QLabel()
        inc.image_lbl.setPixmap(QPixmap(inc.image).scaled(64, 64))
        inc.upgrade_btn = QPushButton(f"Upgrade for: {inc.upgrade_cost} $")
        inc.upgrade_btn.setFont(self.adv_cap_font_small)
        inc.upgrade_buy_counter_btn = QPushButton(f"x{inc.upg_x[inc.upg_buy_counter]}")
        inc.upgrade_buy_counter_btn.clicked.connect(inc.upgrade_buy_counter_handle)
        inc.upgrades_no_lbl = QLabel()
        inc.upgrades_no_lbl.setNum(inc.upgrades_no)
        inc.upgrades_no_lbl.setFont(self.adv_cap_font_small)

        inc.layout = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(inc.upgrade_btn)
        hbox.addWidget(inc.upgrades_no_lbl)
        hbox.addWidget(inc.upgrade_buy_counter_btn)

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
        if self.data.money >= inc.upgrade_cost * inc.upg_x[inc.upg_buy_counter]:

            if inc.index not in self.threads:
                self.threads[inc.index] = PrThread(inc=inc, index=inc.index)
                self.threads[inc.index].change_value.connect(self.setProgressValue)
                self.threads[inc.index].start()
                self.data.money -= inc.upgrade_cost * inc.upg_x[inc.upg_buy_counter]
                inc.upgrades_no += inc.upg_x[inc.upg_buy_counter]
            else:
                inc.upgrades_no += inc.upg_x[inc.upg_buy_counter]
                self.data.money -= inc.upgrade_cost * inc.upg_x[inc.upg_buy_counter]
        else:
            return

    def setProgressValue(self, val):
        index = self.sender().index

        self.data.incs[index - 1].pr_bar.setValue(val)

    # update view
    def update_labels(self):
        self.money_label.setText(f'Money: {self.data.money} $')
        for inc in self.data.incs:
            inc.upgrades_no_lbl.setNum(inc.upgrades_no)
            inc.upgrade_buy_counter_btn.setText(f"x{inc.upg_x[inc.upg_buy_counter]}")

    def increase_money(self):
        self.data.money += 1
        self.update_labels()
