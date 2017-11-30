# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/index.htm')
time.sleep(1)
driver.find_element_by_xpath('//*[contains(text(),"Link Test")]').click()
# driver.implicitly_wait(30)
# m = driver.find_element_by_link_text("linkByContent")
# m.click()
# time.sleep(1)
# print driver.title
# driver.back()
# link with return
driver.find_element_by_link_text('link with return true').click()
# time.sleep(2)
t = driver.switch_to_alert()
print t.text
t.accept()
driver.find_element_by_xpath('//input[@name="t1"]').send_keys(u'和毛钱')
driver.find_element_by_xpath('//input[@name="c1"]').click()
time.sleep(1)
# driver.find_element_by_xpath('//input[@value="cv3"').click()
driver.find_element_by_xpath('/html/body/form/input[5]').click()
radio = driver.find_element_by_xpath('//input[@value="rv2"]')
radio.click()
if radio.is_selected():
    print 'Radio is selected!'

# js = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
# 谷歌浏览器操作滚动条
# js = 'var q=document.body("scroll")[0].scrollTop=1000'
# js = 'var q=document.documentElement.srollTop=2000'
# 滚动条回到最底部
# js='window.scrollTo(0,document.body.scrollHeight)'
# js = 'window.scrollTo(0,1/4（document.body.scrollHeight）)'
# 滚动条定位到元素所在的位置
target = driver.find_element_by_xpath('/html/body/form/input[5]')
driver.execute_script('arguments[0].scrollIntoView();", target')
# driver.execute_script(js)
# driver.quit()


# select 选择
# se = Select(driver.find_element_by_id('s1Id'))
# se.select_by_value('o3')
# print driver.getattrbute()
