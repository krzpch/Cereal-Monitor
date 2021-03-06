from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import monitor_gui as gui

def main_window():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Cereal Monitor")
    MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

    MainWindow.show()
    sys.exit(app.exec_())

main_window()
