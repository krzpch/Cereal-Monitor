.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/


==============
Cereal-Monitor
==============


    This project is a gui based serial monitor that enables sending and receiving data through serial ports.
   

A longer description of your project goes here...



.. image:: https://github.com/krzpch/Cereal-Monitor/blob/main/Screenshot.png
  :width: 800
  :alt: Alternative text

Documentation
====
 
class UARTPort(QThread):
 
.. code:: python

    def run(self):
        while self.port_opened:
            temp_data = self.serial_port.read_all()
            self.recv.emit(temp_data)
            self.data = temp_data


Dependencies
====
PyQt5 : https://pypi.org/project/PyQt5/
 
pySerial  : https://pypi.org/project/pyserial/

Note
====

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
