import sys
import socket
from datetime import *
#localIP = socket.gethostbyname(socket.gethostname()
#print 'Please input Local IP: '
localIP = raw_input("Please input Local IP:")
#print 'Local_IP:',HOST,':',PORT
HOST = localIP
PORT = 2010
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Waiting for Connecting...')
conn, addr = s.accept()
print 'Connected by', addr
while 1:
        data1 = conn.recv(1024)
        data2 = data1.encode('hex')
#        data3 = int(data2,16)
        year = data2[:4]
        year1 = int(year,16)
        month = data2[4:8]
        month1 = int(month,16)
        week = data2[8:12]
        week1 = int(week,16)
        day = data2[12:16]
        day1 = int(day,16)
        hour = data2[16:20]
        hour1 = int(hour,16)
        minute = data2[20:24]
        minute1 = int(minute,16)
        second = data2[24:28]
        second1 = int(second,16)
        milisecond = data2[28:32]
        milisecond1 = int(milisecond,16)
        commandno = data2[32:40]
        commandno1 = int(commandno,16)
        pvalue1 = data2[40:44]
        pvalue2 = data2[44:48]
        pvalue3 = data2[48:52]
        pvalue4 = data2[52:56]
        pvalue5 = data2[56:60]
#        data4 = int(data2,16)
#        t1=datetime.now()
#        t2 = t1.strftime('%Y-%m-%d %H:%M:%S %f')
#        print 'Receive',data2
        print "%s-%s-%s %s:%s:%s:%s,Receive: %s,%s,%s,%s,%s" %(year1,month1,day1,hour1,minute1,second1,milisecond1,pvalue1,pvalue2,pvalue3,pvalue4,pvalue5)
        #date2= conn.recv(1024).encode('hex')
        log = file('log.txt', 'a+')
#        log.write(t2 + ',Receive: ' + data2 + '\n')
        log.write("%s-%s-%s %s:%s:%s:%s,Receive: %s,%s,%s,%s,%s" %(year1,month1,day1,hour1,minute1,second1,milisecond1,pvalue1,pvalue2,pvalue3,pvalue4,pvalue5) + '\n')
        log.close()
        if not data1 : break
#        conn.sendall(data)
conn.close()

