# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread as thr, endl

import sys
import glob
import serial

import monitor_serial
import serial_monitor_presets

class Ui_MainWindow(object):
    monitor_presets = serial_monitor_presets.MonitorPresets()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.BaudrateInput = QtWidgets.QLineEdit(self.centralwidget)
        self.BaudrateInput.setGeometry(QtCore.QRect(810, 80, 191, 22))
        self.BaudrateInput.setObjectName("BaudrateInput")
        self.BaudrateInput.setText("9600")

        self.PortBox = QtWidgets.QComboBox(self.centralwidget)
        self.PortBox.setGeometry(QtCore.QRect(810, 30, 191, 22))
        self.PortBox.setObjectName("PortBox")
        # add avaliable ports to list
        for port in self.list_ports():
            self.PortBox.addItem(port, port)

        self.PortLabel = QtWidgets.QLabel(self.centralwidget)
        self.PortLabel.setGeometry(QtCore.QRect(810, 10, 191, 16))
        self.PortLabel.setObjectName("PortLabel")
        self.PortLabel.setText("Port")

        self.BaudrateLabel = QtWidgets.QLabel(self.centralwidget)
        self.BaudrateLabel.setGeometry(QtCore.QRect(810, 60, 111, 16))
        self.BaudrateLabel.setObjectName("BaudrateLabel")
        self.BaudrateLabel.setText("Baudrate")

        self.ParityBox = QtWidgets.QComboBox(self.centralwidget)
        self.ParityBox.setGeometry(QtCore.QRect(810, 130, 191, 22))
        self.ParityBox.setObjectName("ParityBox")
        self.ParityBox.addItem("NONE", 0)
        self.ParityBox.addItem("EVEN PARITY", 1)
        self.ParityBox.addItem("ODD PARITY", 2)
        self.ParityBox.addItem("MARK PARITY", 3)
        self.ParityBox.addItem("SPACE PARITY", 4)

        self.StopbitBox = QtWidgets.QComboBox(self.centralwidget)
        self.StopbitBox.setGeometry(QtCore.QRect(810, 180, 191, 22))
        self.StopbitBox.setObjectName("StopbitBox")
        self.StopbitBox.addItem("ONE", 0)
        self.StopbitBox.addItem("ONE POINT FIVE", 1)
        self.StopbitBox.addItem("TWO", 2)

        self.BytesizeBox = QtWidgets.QComboBox(self.centralwidget)
        self.BytesizeBox.setGeometry(QtCore.QRect(810, 230, 191, 22))
        self.BytesizeBox.setObjectName("BytesizeBox")
        self.BytesizeBox.addItem("8", 0)
        self.BytesizeBox.addItem("7", 3)
        self.BytesizeBox.addItem("6", 2)
        self.BytesizeBox.addItem("5", 1)

        self.ParityLabel = QtWidgets.QLabel(self.centralwidget)
        self.ParityLabel.setGeometry(QtCore.QRect(810, 110, 55, 16))
        self.ParityLabel.setObjectName("ParityLabel")
        self.ParityLabel.setText("Parity")

        self.sfcBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sfcBox.setGeometry(QtCore.QRect(810, 260, 161, 21))
        self.sfcBox.setObjectName("sfcBox")
        self.sfcBox.setText("Software flow controll")

        self.rtsctsBox = QtWidgets.QCheckBox(self.centralwidget)
        self.rtsctsBox.setGeometry(QtCore.QRect(810, 290, 81, 20))
        self.rtsctsBox.setObjectName("rtsctsBox")
        self.rtsctsBox.setText("RTC/CTS")

        self.dsrdtrBox = QtWidgets.QCheckBox(self.centralwidget)
        self.dsrdtrBox.setGeometry(QtCore.QRect(810, 320, 81, 20))
        self.dsrdtrBox.setObjectName("dsrdtrBox")
        self.dsrdtrBox.setText("DSR/DTR")

        self.StopbitsLabel = QtWidgets.QLabel(self.centralwidget)
        self.StopbitsLabel.setGeometry(QtCore.QRect(810, 160, 55, 16))
        self.StopbitsLabel.setObjectName("StopbitsLabel")
        self.StopbitsLabel.setText("StopBits")

        self.BytesizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.BytesizeLabel.setGeometry(QtCore.QRect(810, 210, 111, 16))
        self.BytesizeLabel.setObjectName("BytesizeLabel")
        self.BytesizeLabel.setText("Byte Size")

        self.MainMonitorWindow = QtWidgets.QTextEdit(self.centralwidget)
        self.MainMonitorWindow.setGeometry(QtCore.QRect(20, 10, 751, 720))
        self.MainMonitorWindow.setObjectName("MainMonitorWindow")

        #### open and close buttons ####
        self.OpenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_on_click())
        self.OpenButton.setGeometry(QtCore.QRect(810, 350, 191, 28))
        self.OpenButton.setObjectName("OpenButton")
        self.OpenButton.setText("Open/Change")

        self.CloseButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.close_on_click())
        self.CloseButton.setGeometry(QtCore.QRect(810, 390, 191, 28))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setText("Close")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
        self.menubar.setObjectName("menubar")

        #### Preset saving and loading ####
        self.PresetLabel = QtWidgets.QLabel(self.centralwidget)
        self.PresetLabel.setGeometry(810, 470, 191, 16)
        self.PresetLabel.setObjectName("PresetLabel")
        self.PresetLabel.setText("Saved Presets")

        self.PresetBox = QtWidgets.QComboBox(self.centralwidget)
        self.PresetBox.setGeometry(810, 490, 191, 22)
        self.PresetBox.setObjectName("PresetBox")
        
        self.list_presets()

        self.PresetNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.PresetNameLabel.setGeometry(810, 520, 191, 16)
        self.PresetNameLabel.setObjectName("PresetNameLabel")
        self.PresetNameLabel.setText("Name")

        self.PresetNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.PresetNameLine.setGeometry(810, 540, 191, 22)
        self.PresetNameLine.setObjectName("PresetNameLine")

        self.PresetLoadButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.presetload_on_click())
        self.PresetLoadButton.setGeometry(810, 570, 93, 28)
        self.PresetLoadButton.setObjectName("PresetLoadButton")
        self.PresetLoadButton.setText("Load")

        self.PresetSaveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.presetsave_on_click())
        self.PresetSaveButton.setGeometry(810, 610, 93, 28)
        self.PresetSaveButton.setObjectName("PresetSaveButton")
        self.PresetSaveButton.setText("Save")

        self.PresetDeleteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.presetdelete_on_click())
        self.PresetDeleteButton.setGeometry(810, 650, 93, 28)
        self.PresetDeleteButton.setObjectName("PresetDeleteButton")
        self.PresetDeleteButton.setText("Delete")

        #### String Sending ####
        self.SendStringLabel = QtWidgets.QLabel(self.centralwidget)
        self.SendStringLabel.setGeometry(20, 780, 651, 16)
        self.SendStringLabel.setObjectName("SendStringLabel")
        self.SendStringLabel.setText("Send String")

        self.SendStringLine = QtWidgets.QLineEdit(self.centralwidget)
        self.SendStringLine.setGeometry(20, 800, 651, 31)
        self.SendStringLine.setObjectName("SendStringLine")
        self.SendStringLine.returnPressed.connect(self.send_on_click)

        self.SendStringButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.send_on_click())
        self.SendStringButton.setGeometry(680, 800, 93, 31)
        self.SendStringButton.setObjectName("SendStringButton")
        self.SendStringButton.setText("Send")

        self.IncludeNBox = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeNBox.setGeometry(690, 840, 651, 31)
        self.IncludeNBox.setObjectName("IncludeNBox")
        self.IncludeNBox.setText("\\n")

        self.IncludeRBox = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeRBox.setGeometry(730, 840, 651, 31)
        self.IncludeRBox.setObjectName("IncludeRBox")
        self.IncludeRBox.setText("\\r")

        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.set_port_status()
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    #### open and clsoe the serial port for reading and writing ####
    def set_port_status(self):
        self.port_opened = False

    def open_on_click(self):
        self.UARTThread = monitor_serial.UARTPort(self.PortBox.currentData(),self.BaudrateInput.text(),
            self.ParityBox.currentIndex(),self.StopbitBox.currentIndex(), self.BytesizeBox.currentIndex(), 
            self.sfcBox.isChecked(), self.rtsctsBox.isChecked(), self.dsrdtrBox.isChecked())
        self.UARTThread.recv.connect(self.display_data)
        self.UARTThread.setTerminationEnabled(True)
        self.UARTThread.start()
        self.port_opened = True

    def close_on_click(self):
        self.UARTThread.close_port()
        self.port_opened = False

    def display_data(self, data):
        self.MainMonitorWindow.moveCursor(QtGui.QTextCursor.MoveOperation.End)
        self.MainMonitorWindow.insertPlainText(data)
        self.MainMonitorWindow.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    #### String Sending ####
    def send_on_click(self):
        if self.port_opened:
            self.UARTThread.send(self.SendStringLine.text())

    #### preset load, save and delete button ####
    def presetload_on_click(self):
        port_available = False

        port, baudrate, parity, stopbits, bytesize, sfc, rtscts, dsrdtr = self.monitor_presets.load_preset(self.PresetBox.currentText())

        for i in range(self.PortBox.count()):
            if self.PortBox.itemText(i) == port:
                port_available = True
        
        if port_available == False:
            ## TODO: impement error message ;-)
            print('nie ma takiego portu, szefunciu')
        else:
            self.PortBox.setCurrentText(port)
            self.BaudrateInput.setText(baudrate)
            self.ParityBox.setCurrentIndex(parity)
            self.StopbitBox.setCurrentIndex(stopbits)
            self.BytesizeBox.setCurrentIndex(bytesize)
            self.sfcBox.setChecked(sfc)
            self.rtsctsBox.setChecked(rtscts)
            self.dsrdtrBox.setChecked(dsrdtr)


    def presetsave_on_click(self):
        self.monitor_presets.save_preset(self.PresetNameLine.text(), self.PortBox.currentData(), self.BaudrateInput.text(),
            self.ParityBox.currentIndex(), self.StopbitBox.currentIndex(), self.BytesizeBox.currentIndex(), 
            self.sfcBox.isChecked(), self.rtsctsBox.isChecked(), self.dsrdtrBox.isChecked())
        
        self.PresetBox.clear()
        self.list_presets()

    def presetdelete_on_click(self):
        self.monitor_presets.delete_preset(self.PresetBox.currentText())
        
        self.PresetBox.clear()
        self.list_presets()

    def list_presets(self):
        for preset in self.monitor_presets.data['presets']:
            self.PresetBox.addItem(preset['name'])

    # avaliable port detection
    def list_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/ttyS[0-90-9]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
