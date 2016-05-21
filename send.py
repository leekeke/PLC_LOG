import socket
HOST = '192.111.111.201'
PORT = 2011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
       data1 = raw_input("Please input cmd:")
       data2 = data1.encode('hex')
       print data1
       print data2
       cmd = str(data1)
       print cmd
       s.sendall(cmd)
       data = s.recv(1024)
       print data
       if not data:
           s.close()
s.close()