import socket
from datetime import *
HOST = '192.111.111.33'                 # Symbolic name meaning all available interfaces
PORT = 2010              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Waiting for Connecting...')
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    t1=datetime.now()
    t2 = t1.strftime('%Y-%m-%d %H:%M:%S %f')
    print t2,' , ',data
    log = file('log.txt', 'a+')
    log.write(t2)
    log.write(' : ')
    log.write(data)
    log.write('\n')
    log.close()
    if not data: break
    conn.sendall(data)
conn.close()