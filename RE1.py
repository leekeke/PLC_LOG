#!/usr/bin/evn python
#coding:utf-8

import socket
import threading

host = '192.111.111.33'
port = 8805
username = ''
clients = []

def server(sock, addr):
    while 1:
        try:
            print 'waitting data...'
            data = sock.recv(1024)
            if not data:
                break
            for c in clients:
                c.send(data)
            print data
        except:
            break
    clients.remove(sock)
    sock.close()
    print '[%s:%s] leave' % (addr[0], addr[1])
    print clients

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket create'
s.bind((host, port))
s.listen(3)
print 'Socket is listenning...'

while 1:
    client, addr = s.accept()
    username = client.recv(1024)
    clients.append(client)
    print '[%s:%s:%s] join!' % (addr[0], addr[1], username)
    print clients

    thread = threading.Thread(target = server, args = (client, addr))
    thread.start()