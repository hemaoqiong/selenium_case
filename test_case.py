# coding=utf-8
import os

caselist = os.listdir('/home/forin/WorkSpace/testcase')
for a in caselist:
    s = a.split('.')[1]
    if s == 'py':
        os.system('/home/forin/WorkSpace/testcase/log.txt')
       # print 'aa'
