import sys
import socket
from datetime import *
import xlrd

def excel_rd():
        excel_data = xlrd.open_workbook('par_data.xls')
        table = excel_data.sheets()[0]
        global localip,dwell_T2
        localip = table.cell(0,1).value
        dwell_T = table.cell(1,1).value
        dwell_T2 =int(dwell_T)

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

def coll_data():
        while 1:
                data1 = conn.recv(1024)
                data2 = data1.encode('hex')
                log_date = data2[:32]
                x = len(log_date)
                log_date1 = [int(log_date[i*4:(i+1)*4],16) for i in range(0,x/4) ]
                year = log_date1[:1]
                month = log_date1[1:2]
                week = log_date1[2:3]
                day = log_date1[3:4]
                hour = log_date1[4:5]
                minute = log_date1[5:6]
                second = log_date1[6:7]
                milisecond = log_date1[7:8]
                pvalue1 = int(data2[32:36],16)
                pvalue2 = int(data2[36:40],16)
                pvalue3 = int(data2[40:44],16)
                pvalue4 = int(data2[44:48],16)
                pvalue5 = int(data2[48:52],16)

                if pvalue3 == 1:
                        pvalue2 = pvalue2-65536

                print "%s-%s-%s %s:%s:%s:%s,Receive: %s,%s,%s,%s,%s" %(year,month,day,hour,minute,second,milisecond,pvalue1,pvalue2,pvalue3,pvalue4,pvalue5)

                log = file('log.txt', 'a+')
                log.write("%s-%s-%s %s:%s:%s:%s,Receive: %s,%s,%s,%s,%s" %(year,month,day,hour,minute,second,milisecond,pvalue1,pvalue2,pvalue3,pvalue4,pvalue5) + '\n')
                if not data1 : break
        conn.close()

if __name__ == '__main__':
        excel_rd()
        tcp_con()
        coll_data()



