import sys
from Log_Recorder import *
from PyQt4.QtGui import *
import receive
from threading import Thread

class IPCThread(receive):
    def __init__(self):
        Thread.__init__(self)

class PlcLog(QDialog,Ui_PLC_LogRecorder):
    def __init__(self, parent= None):
        super(PlcLog,self).__init__(parent)
        self.setupUi(self)
        self.Set_Button.clicked.connect(receive)

class ReceiveLog(receive):
    def ReceiveDate(self):
        Rdate = str(receive.date1)
        self.ipc = IPCThread()
        self.Log_Browser.setText(Rdate)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = PlcLog()
    dlg.show()
    app.exec_()
