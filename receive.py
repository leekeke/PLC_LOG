#coding:utf-8
import socket                   #载入socket模块
import time                     #载入读取系统时间模块
import xlrd                     #载入excel模块

def excel_rd():                 #定义excel读取功能
        global localip,localport,data_len1,data_len2            #定义全局变量：IP，端口，起始字段，结束字段
        excel_data = xlrd.open_workbook('par_data.xls')         #打开excel配置表
        table = excel_data.sheets()[0]                  #定义table变量是数据表1
        localip = table.cell(0,1).value                 #读取IP地址
        localport = int(table.cell(1,1).value)          #读取Port地址，读取到的是浮点数，需要转化为整数
        data_len1 = int(table.cell(2,1).value)          #读取日志起始字段
        data_len2 = int(table.cell(3,1).value)          #读取日志结束字段

def tcp_con():                  #定义tcp连接功能
        HOST = localip
        PORT = localport
        print "Reading local IP..."
        print 'Local_IP:',HOST,', Port:',PORT
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)          #使用套接字建立连接
        s.bind((HOST, PORT))            #绑定IP及端口
        s.listen(1)
        print('Waiting for Connecting...')
        global conn
        conn, addr = s.accept()         #这里的addr是tuple变量
        loctime =time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
        print 'Local Time: %s, Connected by %s' % (loctime,str(addr))
        log = file('log.txt', 'a+')
        log.write('Local Time: %s, Connected by %s' % (loctime,str(addr)) + '\n') #这里的Local Time是计算机时间

def coll_data():                #定义数据获取功能
        while 1:                #一直循环
                raw_data = conn.recv(1024)         #最大获取1024个word，收到的数据为string形式
                data16 = raw_data.encode('hex')     #转码为16进制
                plc_time = data16[:32]           #PLC时间为数据前32个byte（前16个word）
                log_data = data16[32:]              #byte32之后是日志数据
                x = len(plc_time)               #获取plc_time数据长度
                z = [int(plc_time[i*4:(i+1)*4],16) for i in range(0,x/4) ]
                #将PLC时间转码为16进制整数，并存储到列表z中，i的循环次数是0--x/4
                p = [int(log_data[q*4:(q+1)*4],16) for q in range(data_len1-1,data_len2) ]
                #将日志数据转码为16进制，并存储到列表p中
                print 'PLC Time: %s-%s-%s %d:%d:%d:%d Receive: %r' %(z[0],z[1],z[3],z[4],z[5],z[6],z[7],p)
                log1 = file('log.txt', 'a+')
                log1.write('PLC Time: %s-%s-%s %d:%d:%d:%d, Receive: %r'
                          %(z[0],z[1],z[3],z[4],z[5],z[6],z[7],p) + '\n')
                if not raw_data : break
        conn.close()

if __name__ == '__main__':              #主程序，按顺序调用功能
        excel_rd()
        tcp_con()
        coll_data()



