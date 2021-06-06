import sys
from classes import Data
from classes import MainWindow
from PyQt5.QtWidgets import QApplication
from classes import MyThread


def exit_handler():
    thread1.quit()
    thread1.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(exit_handler)
    window = MainWindow()
    thread1 = MyThread(window)
    thread1.start()
    sys.exit(app.exec_())
