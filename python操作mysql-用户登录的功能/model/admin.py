#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utility.sql_helper import MySqlHelper


class Admin():
    def __init__(self):
        self.__helper = MySqlHelper()

    def CheckValidate(self, username, password):
        sql = "select * from admin where username=%s and password=%s"
        params = (username, password)
        return self.__helper.getOne(sql, params)
