#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql
import conf

# 在操作数据库的时候，python2中一般使用mysqldb，但在python3中已经不在支持mysqldb了，我们可以用pymysql和mysql.connector。本文的所有操作都是在python3的pymysql下完成的。
# http://www.cnblogs.com/whatisfantasy/p/6134660.html


class MySqlHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict  # 把数据库连接信心提取到conf中

    def getDict(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)
        # cur = conn.cursor()
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建cursor的时候，指定1其返回的cursor类型为dict

        cur.execute(sql, params)    # 返回受影响的行数
        data = cur.fetchall()   # 返回数据,返回的是tuple类型
        cur.close()
        conn.close()
        return data

    def getOne(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)  # 加**后表示传入的是字典里的数据，否则报错
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, params)
        data = cur.fetchone()  # 使用fechone来逐条获取数据
        cur.close()
        conn.close()
        return data
