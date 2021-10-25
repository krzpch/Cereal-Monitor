import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

#translation dictionaries
parity_dic = {0 : serial.PARITY_NONE, 1 : serial.PARITY_ODD, 2: serial.PARITY_EVEN, 3 : serial.PARITY_MARK, 4: serial.PARITY_SPACE}
stopbit_dic = {0 : serial.STOPBITS_ONE, 1 : serial.STOPBITS_ONE_POINT_FIVE, 2 : serial.STOPBITS_TWO}
bytesize_dic = {0 : serial.EIGHTBITS, 1 : serial.FIVEBITS, 2 : serial.SIXBITS, 3 : serial.SEVENBITS}

class UARTPort(QThread):
    def _UARTPort__init(self, port, baudrate, parity, stopbit, bytesize, sfc, rtscts, dsrdtr) -> None:
        QThread.__init(self)
        # set basic settings
#        self.port = None
#        self.baudrate = 9600
#        self.parity = parity_dic[0]
#        self.stopbit = stopbit_dic[0]
#        self.bytesize = bytesize_dic[0]
        self.timeout = None
#        self.sfc = False
#        self.rtscts = False
#        self.dsrdtr = False
        self.writetimeout = None
        self.serial_port = serial.Serial(port, baudrate, 
            bytesize_dic[bytesize], parity_dic[parity], stopbit_dic[stopbit], self.timeout,
            sfc, rtscts, self.writetimeout ,dsrdtr)
        if self.serial_port.is_open:
            self.port_opened = True
        else:
            self.port_opened = False

    def run(self):
        while self.port_opened:
            raise NotImplementedError


    def close_port(self):
        if self.port_opened == True:
            self.serial_port.close()
        self.terminate()

    