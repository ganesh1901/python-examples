import os


class Others:
    def __init__(self):
        self.data = ''


class FIFO:
    try:
        data_pipe = ""  # file descripter of tx_fifo in non blocking mode
        rx_fifo = "/tmp/cmd_fifo"  # named fifo for sending command
        tx_fifo = "/tmp/rsp_fifo"  # named fifo for receiving response
        err_fifo = "/tmp/err_fifo"
        surveillance_fifo = "/tmp/sur_fifo"
        ins_fifo = "/tmp/ins_fifo"

        surveillance_info_fifo = ''
        error_info_pipe = ""
        fifo_in = -1
        ins_info_fifo = ''
        e_poll = ''
        error_e_poll = ""
        surveillance_epoll = ''
        ins_epoll = ''
        poll_timeout = 1
        max_fifo_size = 512

        cmd_fd = os.open(rx_fifo, os.O_RDWR | os.O_NONBLOCK)
        print 'cmd fifo', cmd_fd

        rsp_fd = os.open(tx_fifo, os.O_RDWR | os.O_NONBLOCK)
        print 'rsp fifo ', rsp_fd

        sur_fd = os.open(surveillance_fifo, os.O_NONBLOCK | os.O_RDWR)
        print 'sur fifo', sur_fd



    except IOError:
        print 'at fifo open '
