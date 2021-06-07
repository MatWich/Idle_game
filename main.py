import sys

from PyQt5 import QtCore

from classes import Data
from classes import MainWindow
from PyQt5.QtWidgets import QApplication
from classes import MyThread
import threading

from settings import *


def exit_handler():
    pass



if __name__ == '__main__':
    print(LEMON_IMG)
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(exit_handler)
    window = MainWindow()



    sys.exit(app.exec_())
