# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get('http://bj.ganji.com/')
# driver.implicitly_wait(20)
time.sleep(3)
h = driver.current_window_handle  # 获取当前窗口句柄
# driver.find_element_by_xpath('/html/body/div[3]/ul/li/a[5]').click()
search_str = u'招聘求职'
print 'search_str: ' + search_str
print search_str
driver.find_element_by_link_text(search_str).click()
time.sleep(2)
print driver.title


all_h = driver.window_handles  # 获取所有句柄
print all_h
# 循环判断是否与首页句柄相等
for i in all_h:              # 切换窗口
    if i != h:
        driver.switch_to.window(i)
        print driver.title   # 打印切换窗口的title
driver.close()               # 关闭当前窗口
driver.switch_to.window(h)   # 切到句柄首页
print driver.title           # 打印首页标题
driver.quit()
