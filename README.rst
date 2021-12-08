.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/


==============
Cereal-Monitor
==============


    This project is a gui based serial monitor that enables sending and receiving data through serial ports.
   

To use this program you nned to start script named monitor_main.py. It automatically check all avaliable ports and shows them in port box. After this you can set desired settings and then you press "Connect/Change" button. You can send data by writing it to "Send String" box and presing "Send". The mesage is send as string. Second option is using keyboard in main window. Using this method sends every character independently. Moreover, you can check "\\n' or "\\r" checkbox to add this white characters to the end of string. 

.. image:: https://github.com/krzpch/Cereal-Monitor/blob/main/screenshots/screen2.png
  :width: 800
  :alt: Alternative text

"Show White Characters" allows you to see "\\n" and "\\r" on main widnow. 

.. image:: https://github.com/krzpch/Cereal-Monitor/blob/main/screenshots/screen0.png
  :width: 800
  :alt: Alternative text


"Show Hex Format" checkbox allows you to convert all received data to hexadecimal values. This mode allows you to read data whitch cannot be represented in UTF-8 enoding or white characters. 

.. image:: https://github.com/krzpch/Cereal-Monitor/blob/main/screenshots/screen1.png
  :width: 800
  :alt: Alternative text

Additionally you can save your active preset and load it in next use of this program. 

To correctly use this you must:
 - set desired port and other settings
 - write the name of this preset
 - press "Save" button

To apply saved prestes you need to select desired preset form list and click "Load" button. If desired port is avaliable, the preset will be loaded to your current settings.




==============
Documentation
==============
 
Class representing window. Contains methods for displaying ui elements and handling interactions with user.
====
.. code:: python

    class Ui_MainWindow(object):

Method for initialization of main interface.

.. code:: python

    def setupUi(self, MainWindow):

Method for clearing main window.

.. code:: python

    def clear_main_window_on_click(self):
    
Method for setting serial port status.

.. code:: python
    
    def set_port_status(self):

Metod for listing available ports.

.. code:: python

    def list_ports(self):

Metods for opening/closing serial port with selected parameters.

.. code:: python

    def open_on_click(self):
    def close_on_click(self):
    
Metod for displaying data received from serial port.

.. code:: python

    def display_data(self, data):

Metod for sending data from input box through serial port.

.. code:: python

    def send_on_click(self):

Metods for preset handling (adding new preset, deleting, loading, listing existing).

.. code:: python

    def presetload_on_click(self):
    def presetsave_on_click(self):
    def presetdelete_on_click(self):
    def list_presets(self):

Metods for handling keyboard input.

.. code:: python

    def keyPressEvent(self, event):
    def keyReleaseEvent(self, event):


Class representing serial port. Contains methods for handling serial communication.
====
.. code:: python

    class UARTPort(QThread):

Method for reading data from rx buffer.

.. code:: python

    def run(self):

Methods for sending and receiving data.

.. code:: python

    def recv_string(self):
    def send(self, data):
    
Method for closing serial port.

.. code:: python

    def close_port(self):    



Class for handling presets saved in .json file.
====
.. code:: python

    class MonitorPresets():

Methods for adding, removing, and loading serial port presets.

.. code:: python

    def save_preset(self, name, port, baudrate, parity, stopbits, bytesize, sfc, rtscts, dsrdtr):
    def load_preset(self, name):
    def delete_preset(self, name):



==============
Dependencies
==============
PyQt5 : https://pypi.org/project/PyQt5/
 
pySerial  : https://pypi.org/project/pyserial/

==============
Note
==============

TESTED ONLY ON WINDOWS!

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
