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

        menubar = self.menuBar()
        about = menubar.addMenu('&About')
        setting = menubar.addMenu('&Settings')
        help = menubar.addMenu('&Help')
        self.show()

        action1 = QtGui.QAction("Controller", self)
        action2 = QtGui.QAction("GUI", self)

        about.addAction(action1)
        about.addAction(action2)

        action1.triggered.connect(self.dialog1)
        action2.triggered.connect(self.dialog2)

    def dialog2(self):
        dia2 = QtGui.QDialog()
        dia2.setWindowTitle(" Dialog2 ")
        dia2.exec_()

    def dialog1(self):
        dia1 = QtGui.QDialog()
        # show() will be called with background process / modal
        #dia1.show()
        ret = dia1.exec_()
        if ret == QtGui.QDialog.Accepted:
            print 'yes'
        else:
            print 'no'
        #dia1.setModal(True)


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