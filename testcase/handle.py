# coding=utf-8
from selenium import webdriver
import time
import os


# def Handle()

fp = open('/home/forin/WorkSpace/testcase/handel.txt', 'r')
text = fp.readlines()
print text
fp.close()
for arg in text:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get("http://bj.ganji.com/")
    time.sleep(5)
    h = driver.current_window_handle
    print repr(arg[:-1].decode('utf-8'))
    s = driver.find_element_by_link_text(arg[:-1].decode('utf-8'))
    s.click()
    all_h = driver.window_handles
    for i in all_h:
        if i != h:
            driver.switch_to.window(i)
            print "now handle is " + i
            print driver.title
        if arg in driver.tile:
            print "页面打开正常"
        else:
            print '测试失败'

        driver.close()
        driver.switch_to.window(h)
