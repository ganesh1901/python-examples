import signal
import sys

def handler(signum):
    print 'at handler---',signum

if __name__ == "__main__":

    signal.signal(signal.SIGHUP, handler)
