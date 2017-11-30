# coding=utf-8
# name='he'
# age=39
# print'my name is %s' %name
# print'my age is %s' %age
# print 'my age is %s,my name is %s' %(age,name)

import xlrd
data = xlrd.open_workbook("/home/forin/login.xlsx")
table = data.sheet_by_name(u'工作表1')
row = table.nrows
col = table.ncols

print table.row_values(0)  # 答应第一行
print table.row_values(1)  # 答应第二行
print table.col_slice(0)   # 答应第一列
print "打印第二列"
print table.col_slice(1)
