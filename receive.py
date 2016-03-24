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
        t1=datetime.now()
        t2 = t1.strftime('%Y-%m-%d %H:%M:%S %f')
        print t2+',Receive',data2
        #date2= conn.recv(1024).encode('hex')
        log = file('log.txt', 'a+')
        log.write(t2 + ',Receive: ' + data2 + '\n')
        log.close()
        if not data1 : break
#        conn.sendall(data)
conn.close()

