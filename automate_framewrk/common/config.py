# coding=utf-8
import os
import time

# 设置报告文件保存路径


def report(self):
    # filepath = os.path.dirname(os.path.abspath('.')) + '/reports/'
    path = os.path.abspath('.')
    path1 = os.path.join(path, "package")
    filepath = path1 + '/reports/'
    # 获取系统当前时间
    now = time.strftime('%Y%m%d%M%H%S', time.localtime())
    # 设置保存文件的名称格式
    filename = filepath + now + 'HTMLtemplate.html'
    return filename

# 设置logs文件保存路径
# 在log.py里面定义了
# def logs(self):
#     filepath2 = os.path.dirname(os.path.abspath('.')) + '/logs/'
#     now = time.strftime('%Y%m%d%M%H%S', time.localtime())
#     filename2 = filename2 + now + '.log'
