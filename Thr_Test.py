
import receive
import sys
from threading import Thread
from pyqt4 import *

class TCP_IPThread(Thread):
     def __init__(self):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # Setup TCP socket
        self.socket.bind(('192.168.6.1', 2010))
        self.socket.listen(5)
        self.setDaemon(True)
        self.start()

     def run(self):
        while True:
            try:
                client, addr = self.socket.accept()

                ready = select.select([client,],[], [],2)
                if ready[0]:
                    recieved = client.recv(4096)
                    print recieved
                    wx.CallAfter(pub().sendMessage,
                                 "update", recieved)

            except socket.error, msg:
                print "Socket error! %s" % msg
                break
