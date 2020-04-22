from PyQt4 import QtGui, QtCore
import sys
import time


class Example(QtGui.QMainWindow):

    def __init__(self):
        #super(Example, self).__init__()
        QtGui.QMainWindow.__init__(self)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')

        self.menubar = self.menuBar()
        self.menubar.addMenu('&About')
        self.menubar.addMenu('&Settings')
        self.menubar.addMenu('&Help')
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())