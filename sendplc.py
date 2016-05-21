import socket
import xlrd

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

def coll_data():
    while 1:
       data1 = input("Please input cmd:")
#       data2 = data1.encode('hex')
       print data1
#       print data2
       cmd = str(data1)
       print cmd
       conn.send(cmd)
    conn.close()



if __name__ == '__main__':
        excel_rd()
        tcp_con()
        coll_data()