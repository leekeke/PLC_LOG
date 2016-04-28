# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log_Recorder.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import threading
import socket
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.messages = []

        recvThread = threading.Thread(target = self.recvFromServer)
        recvThread.setDaemon(True)
        recvThread.start()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("PLC_LOG"))
        Form.resize(800, 600)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 80, 631, 391))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 510, 112, 34))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("PLC_LOG", "PLC_LOG", None))
        self.pushButton.setText(_translate("PLC_LOG", "Exit", None))


    def recvFromServer(self):
        while 1:
            try:
                data = raw_input('input:')
                if not data:
                    exit()
                self.messages.append(data)
            except:
                return

    def showChat(self):
        for m in self.messages:
            self.textBrowser.append(m)
        self.messages = []

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Form()
    win.show()
    sys.exit(app.exec_())









