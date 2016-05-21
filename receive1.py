import socket
import xlrd
import os
import json
import string

def excel_rd():
        excel_data = xlrd.open_workbook('par_data.xls')
        table = excel_data.sheets()[0]
        global localip,data_len
        localip = table.cell(0,1).value
        data_len = table.cell(1,1).value

def tcp_con():
        HOST = localip
        PORT = 2010
        print "Reading local IP..."
        print 'Local_IP:',HOST,', Port:',PORT
        global s
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        print('Waiting for Connecting...')
        global conn
        conn, addr = s.accept()
        print 'Connected by', addr

def intstr(x):
        int(x,16)

def coll_data():
        while 1:
                data1 = conn.recv(1024)
                data2 = data1.encode('hex')
                print data1
                print data2
                v = map(intstr,(data2))
                print v
                pvalue = data2[3:int(data_len)+4]
                print "Receive:",pvalue
                y = [d for d in pvalue]
                print y
                z = json.dumps(y)
                print z
                u = ' '.join(y)
                print u
                log = file('log.txt', 'a+')
                log.write("Receive: %s" % (pvalue) + '\n')
                conn.sendall(pvalue)
                if not data1: break
        conn.close()

if __name__ == '__main__':
        excel_rd()
        tcp_con()
        coll_data()