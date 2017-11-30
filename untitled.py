
# coding=utf-8
from selenium import webdriver
# import xlrd
import time
from test_xlrd import ExcelUtil


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
        driver.find_element_by_id("passname").clear()
        driver.find_element_by_id("passname").send_keys(lis[t][passname])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(lis[t][password])
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id="content"]/div/div[6]/input").click()
        driver.find_element_by_link_text(u"登录").click()
# if __name__== "__main__":
if __name__ == "__main__":
    login()
