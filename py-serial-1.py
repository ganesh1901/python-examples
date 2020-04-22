import serial
import sys
import glob
from PyQt4 import QtCore, QtHelp, QtGui

class Example(object):
    """
    Handle a connection to an OpenBCI board.

    Args:
      port: The port to connect to.
      baud: The baud of the serial connection.
    """

    def __init__(self, port=None, baud=115200, log=True, timeout=None):
        self.log = log  # print_incoming_text needs log
        self.baudrate = baud
        self.timeout = timeout

        if not port:
            tmp = self.find_port()
            if tmp != '':
                port = tmp[0]
        self.port = port

        self.ser = serial.Serial(port=port, baudrate=baud, timeout=timeout)


    def find_port(self):
        # Finds the serial port names
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/ttyUSB*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.usbserial*')
        else:
            raise EnvironmentError('Error finding ports on your operating system')
        return ports


if __name__ == "__main__":
    print 'before main'
    Example('', 2000000, False, 10)
    print 'after main'

