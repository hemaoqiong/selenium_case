# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
driver.get(url)
driver.maximize_window()
# driver.implicitly_wait(20)
time.sleep(3)
# login first
username = u"胖嘟嘟"
password = "he@12345"
m = driver.find_element_by_id("input1")
m.clear()
m.send_keys(username)
s = driver.find_element_by_id("input2")
s.clear()
s.send_keys(password)
driver.find_element_by_id("remember_me").click()
driver.find_element_by_id("signin").click()
# 创建随笔
time.sleep(2)
title = driver.find_element_by_id("Editor_Edit_txbTitle")
title.clear()
title.send_keys(u"创建随笔")
driver.switch_to_frame("Editor_Edit_EditorBody_ifr")
div = driver.find_element_by_id("tinymce")
div.clear()
text = u"创建随笔现有的单元测试框架单元测试是保证程序正确性的一种有效的测试手段，对于不同的开发语言，通常都能找到相应的单元框架。"
div.send_keys(text)
time.sleep(1)
driver.switch_to.default_content()

# 下拉滚动条
# js = 'document.getElementsByClassName("scroll")[0].scrollTop=1000'
# js = "window.scrollTo=(0,10000)"
js = 'document.body.scrollTop=1000'
# js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
# 发布
# target = driver.find_element_by_id("Editor_Edit_lkbPost")
# 存草稿
target = driver.find_element_by_id("Editor_Edit_lkbDraft")
target.click()
print driver.title
driver.quit()
