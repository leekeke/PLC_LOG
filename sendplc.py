# -*- coding: utf-8 -*-
import socket
import xlrd
import struct

def excel_rd():
        excel_data = xlrd.open_workbook('par_data.xls')
        par_table = excel_data.sheets()[0]
        data_table = excel_data.sheets()[1]
        global localip,data_len,DB_data
        localip = par_table.cell(0,1).value
        data_len = par_table.cell(1,1).value
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
        print DB_data


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
    if conn:
       data1= DB_data
       conn.send(data1)
    conn.close()

if __name__ == '__main__':
        excel_rd()
        tcp_con()
        coll_data()