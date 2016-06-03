def str2byte(s):
    base='0123456789ABCDEF'
    i=0
    s = s.upper()
    s1=''
    while i < len(s):
        c1=s[i]
        c2=s[i+1]
        i+=2
        b1=base.find(c1)
        b2=base.find(c2)
        if b1 == -1 or b2 == -1:
            return None
        s1+=chr((b1 << 4)+b2)
    return s1
s = 'C7 EB CE F0 BE C6 BA F3 BC DD B3 B5'.replace(' ','') #去掉空格
s1 = str2byte(s)
print s1.decode('gbk') #以gbk编码解码输出