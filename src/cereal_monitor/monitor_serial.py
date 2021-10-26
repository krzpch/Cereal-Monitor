import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

#translation dictionaries
parity_dic = {0 : serial.PARITY_NONE, 1 : serial.PARITY_ODD, 2: serial.PARITY_EVEN, 3 : serial.PARITY_MARK, 4: serial.PARITY_SPACE}
stopbit_dic = {0 : serial.STOPBITS_ONE, 1 : serial.STOPBITS_ONE_POINT_FIVE, 2 : serial.STOPBITS_TWO}
bytesize_dic = {0 : serial.EIGHTBITS, 1 : serial.FIVEBITS, 2 : serial.SIXBITS, 3 : serial.SEVENBITS}

class UARTPort(QThread):

    # signals
    recv = QtCore.pyqtSignal(object)

    def __init__(self, port, baudrate, parity, stopbit, bytesize, sfc, rtscts, dsrdtr):
        QThread.__init__(self)
        self.timeout = None
        self.writetimeout = None
        self.serial_port = serial.Serial(port, baudrate, 
            bytesize_dic[bytesize], parity_dic[parity], stopbit_dic[stopbit], self.timeout,
            sfc, rtscts, self.writetimeout ,dsrdtr)
        if self.serial_port.is_open:
            self.port_opened = True
            print("Port succesfully opened")
        else:
            self.port_opened = False
            print("Port could not be opened")

    def run(self):
        while self.port_opened:
            temp_str = str(self.serial_port.read_all(),encoding='ascii')
            self.recv.emit(temp_str)
            self.str = temp_str

    def recv_string(self):
        return self.str

    def send(self, data):
        if self.port_opened:
            print("Sending:",data)
            self.serial_port.write(str.encode(data))
            self.serial_port.flush()

    def close_port(self):
        if self.port_opened == True:
            self.serial_port.close()
            self.port_opened = self.serial_port.is_open
        self.terminate()

    