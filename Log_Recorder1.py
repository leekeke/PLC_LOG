# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log_Recorder.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys      #载入sys模块
import threading        #载入threading模块
from PyQt4 import QtCore, QtGui     #载入pyqt4模块
import socket                   #载入socket模块
import time                     #载入读取系统时间模块
import xlrd                     #载入excel模块
import struct                   #载入格式化参数模块，用于socket发送和接收数据

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
        self.timer = QtCore.QTimer()

        UiThread = threading.Thread(target = self.UiConnect)
        UiThread.setDaemon(True)
        UiThread.start()

    def setupUi(self, Form):            #定义UI布局
        Form.setObjectName(_fromUtf8("PLC_LOG"))
        Form.resize(1280, 1024)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 80, 1024, 768))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1100, 900, 112, 34))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 900, 112, 34))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 900, 112, 34))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 900, 112, 34))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.RecvThread)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.disconn)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SendThread)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("PLC_LOG", "PLC_LOG", None))
        self.pushButton.setText(_translate("PLC_LOG", "Exit", None))
        self.pushButton_2.setText(_translate("PLC_LOG", "Start Recv", None))
        self.pushButton_3.setText(_translate("PLC_LOG", "Stop Recv", None))
        self.pushButton_4.setText(_translate("PLC_LOG", "SendData", None))

    def par_excel_rd(self):                 #定义excel读取功能
        global localip,localport,data_len1,data_len2
        #定义全局变量：IP，端口，起始字段，结束字段，数据变量
        excel_data = xlrd.open_workbook('par_data.xls')         #打开excel配置表
        par_table = excel_data.sheets()[0]                  #定义网络参数 是数据表1
        localip = par_table.cell(0,1).value                 #读取IP地址
        localport = int(par_table.cell(1,1).value)          #读取Port地址，读取到的是浮点数，需要转化为整数
        data_len1 = int(par_table.cell(2,1).value)          #读取日志起始字段
        data_len2 = int(par_table.cell(3,1).value)          #读取日志结束字段

    def DB_excel_rd(self):
        global DB_data
        excel_data = xlrd.open_workbook('par_data.xls')         #打开excel配置表
        data_table = excel_data.sheets()[1]
        DB_RawData = data_table.col_values(1)
        nrows = data_table.nrows
        DB_data=[]
        for i in range(1,nrows-1):
            x = int(DB_RawData[i])
            y= struct.pack('h',x)
            z=y[::-1]
            DB_data.append(z)
        DB_data = ''.join(DB_data)
        DB_data = str(DB_data)
        self.textBrowser.append('Load DB data complate.')

    def DB_dataSend(self):
        if conn:
           sendData= DB_data
           conn.send(sendData)
        conn.close()
        self.textBrowser.append('PLC DB data send finished.')

    def tcp_con(self):                  #定义tcp连接功能
        HOST = localip
        PORT = localport
        tcpMessage = 'Local_IP: %s, Port: %s' % (HOST,PORT)
        self.textBrowser.append(tcpMessage)
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)          #使用套接字建立连接
        s.bind((HOST, PORT))            #绑定IP及端口
        s.listen(1)
        self.textBrowser.append('Waiting for Connecting...')
        global conn,loctime,addr
        conn, addr = s.accept()         #这里的addr是tuple变量
        if conn:
            loctime =time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
            self.textBrowser.append('Local Time: %s, Connected by %s' % (loctime,str(addr)))
            log = file('log.txt', 'a+')
            log.write('Local Time: %s, Connected by %s' % (loctime,str(addr)) + '\n')
            log.close()

    def coll_data(self):        #定义数据获取功能
        while conn:                #一直循环
                raw_data = conn.recv(1024)         #最大获取1024个word，收到的数据为string形式
                if raw_data =='':
                    break
                data16 = raw_data.encode('hex')     #转码为16进制
                plc_time = data16[:32]           #PLC时间为数据前32个byte（前16个word）
                log_data = data16[32:]              #byte32之后是日志数据
                x = len(plc_time)               #获取plc_time数据长度
                z = [int(plc_time[i*4:(i+1)*4],16) for i in range(0,x/4) ]
                #将PLC时间转码为16进制整数，并存储到列表z中，i的循环次数是0--x/4
                p = [int(log_data[q*4:(q+1)*4],16) for q in range(data_len1,data_len2)]
                p =' '.join('%s' % id for id in p)
                #将日志数据转码为16进制，并存储到列表p中
                rMessage = 'PLC Time: %s-%s-%s %d:%d:%d:%d Receive: %r' %(z[0],z[1],z[3],z[4],z[5],z[6],z[7],p)
                self.textBrowser.append(rMessage)
#                print 'PLC Time: %s-%s-%s %d:%d:%d:%d Receive: %r' %(z[0],z[1],z[3],z[4],z[5],z[6],z[7],p)
                log = file('log.txt', 'a+')
                log.write(rMessage + '\n')
                log.close()

    def UiConnect(self):
        self.timer.timeout.connect(self.showChat)

    def showChat(self):
        self.textBrowser.append()
#        self.messages = []

    def RecvThread(self):
        UiThread = threading.Thread(target = self.RecvAction)
        UiThread.setDaemon(True)
        UiThread.start()
        self.pushButton_4.setEnabled(False)

    def SendThread(self):
        UiThread = threading.Thread(target = self.SendAction)
        UiThread.setDaemon(True)
        UiThread.start()

    def RecvAction(self):
        self.par_excel_rd()
        self.tcp_con()
        self.pushButton_2.setEnabled(False)
        self.coll_data()

    def SendAction(self):
        self.DB_excel_rd()
        self.par_excel_rd()
        self.tcp_con()
        self.DB_dataSend()

    def disconn(self):
        conn.shutdown(2)
        conn.close()
        self.textBrowser.append('Local Time: %s, Disconnect by %s' % (loctime,str(addr)))
        self.pushButton_2.setEnabled(True)
        self.pushButton_4.setEnabled(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Form()
    win.show()
    sys.exit(app.exec_())