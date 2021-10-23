import serial


#translation dictionaries
parity_dic = {0 : serial.PARITY_NONE, 1 : serial.PARITY_ODD, 2: serial.PARITY_EVEN, 3 : serial.PARITY_MARK, 4: serial.PARITY_SPACE}
stopbit_dic = {0 : serial.STOPBITS_ONE, 1 : serial.STOPBITS_ONE_POINT_FIVE, 2 : serial.STOPBITS_TWO}
bytesize_dic = {0 : serial.EIGHTBITS, 1 : serial.FIVEBITS, 2 : serial.SIXBITS, 3 : serial.SEVENBITS}

class Serial_funcs:
    def __init__(self) -> None:
        super().__init__()
        # set basic settings
        self.port = None
        self.baudrate = 9600
        self.parity = parity_dic[0]
        self.stopbit = stopbit_dic[0]
        self.bytesize = bytesize_dic[0]
        self.timeout = None
        self.sfc = False
        self.rtscts = False
        self.dsrdtr = False
        self.writetimeout = None
        self.serial_port = serial.Serial(self.port, self.baudrate, 
            self.bytesize, self.parity, self.stopbit, self.timeout,
            self.sfc, self.rtscts, self.writetimeout ,self.dsrdtr)

    def serial_open(self):
        if self.port == None or self.baudrate == 0:
            print("ERROR - Wrong port or baudrate")
        else:
            if self.serial_port.is_open() == True:
                self.serial_port.close()
                self.update_settings()
                self.serial_port.open()
            else:      
                self.update_settings()
                self.serial_port.open()
    
    def set_settings(self, list):
        #todo add assertion
        self.port = list[0]
        self.baudrate = int(list[1])
        self.bytesize = bytesize_dic[list[2]]
        self.parity = parity_dic[list[3]]
        self.stopbit = stopbit_dic[list[4]]
        self.sfc = list[5]
        self.rtscts = list[6]
        self.dsrdtr = list[7]

    def update_settings(self):
        assert self.serial_port.is_open() == False, "ERROR - Port is opened, cannot change settings"
        self.serial_port.port(self.port)
        self.serial_port.baudrate(self.baudrate)
        self.serial_port.bytesize(self.bytesize)
        self.serial_port.parity(self.parity)
        self.serial_port.stopbits(self.stopbit)
        self.serial_port.xonxoff(self.sfc)
        self.serial_port.rtscts(self.rtscts)
        self.serial_port.dsrdtr(self.dsrdtr) 
    