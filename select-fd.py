import select
import os

from perf import read_event

from VarList import Others
from VarList import FIFO

from PyQt4 import QtCore
from PyQt4.QtCore import  QThread

import threading


class Listener(threading.Thread):
    def __init__(self, ot, ff):
        threading.Thread.__init__(self)
        self.ot = ot
        self.ff = ff

    def run(self):
        while True:
            sock_list = [self.ff.cmd_fd, self.ff.rsp_fd, self.ff.sur_fd]
            read_list, write_list, error_list = select.select(sock_list, [], [], 10)
            # print 'read_list ', read_list, 'length ', len(read_list)
            for i in read_list:
                data = os.read(i, 512)
                print ' data from ', i, 'fd -- data  ', data


if __name__ == "__main__":
    ot = Others()
    ff = FIFO()

    listener = Listener(ot, ff)
    listener.start()







