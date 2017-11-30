# encoding: utf-8
from selenium import webdriver
import xlrd
import time


class ExcelUtil():
    def __init__(self, filename, sheetname):
        self.data = xlrd.open_workbook(filename)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取总行数
        self.rows = self.table.nrows
        # 获取总列数
        self.cols = self.table.ncols
        # 获取第一行作为key
        self.keys = self.table.row_values(0)

    def dict_data(self):
        if self.rows <= 1:
            print"总行数小与1"
        else:
            r = []
            j = 1
            for i in range(self.rows - 1):
                s = {}
                # 从第二行取对应values值
                value = self.table.row_values(i + 1)
                for x in range(self.cols):
                    s[self.keys[x]] = value[x]
                    r.append(s)
                    j += 1
                    return r


def login():
    filename = '/home/forin/login.xlsx'
    sheetname = u'工作表1'
    data = ExcelUtil(filename, sheetname)
    # 将结果存到s
    lis = data.dict_data()
    for t in range(len(lis)):
        driver = webdriver.Firefox()
    # 浏览器登录
        driver.get("https://workyun.com/")
        time.sleep(1)
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="passname"]').clear()
        driver.find_element_by_xpath(
            '//*[@id="passname"]').send_keys(lis[t]['passname'])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(lis[t]['password'])
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id="content"]/div/div[6]/input").click()
        driver.find_element_by_link_text(u"登录").click()


if __name__ == "__main__":
    login()
