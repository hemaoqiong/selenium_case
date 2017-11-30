# -*- coding: utf-8 -*-

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get('http://sahitest.com/demo/mouseover.htm')

# # 鼠标移动到此元素，在下面的input框中会显示“Mouse moved”
# write = driver.find_element_by_xpath('//input[@value="Write on hover"]')
# blank = driver.find_element_by_xpath(
#     '//input[@value="Blank on hover"]')  # 鼠标移动到此元素，会清空下面input框中的内容

# result = driver.find_element_by_name('t1')

# action = ActionChains(driver)
# action.move_to_element(write).perform()  # 移动到write，显示“Mouse moved”
# print result.get_attribute('value')

# # action.move_to_element(blank).perform()
# # 移动到距离当前位置(10,50)的点，与上句效果相同，移动到blank上，清空
# action.move_by_offset(10, 50).perform()
# print result.get_attribute('value')

# # 移动到距离blank元素(10,-40)的点，可移动到write上
# action.move_to_element_with_offset(blank, 10, -40).perform()
# print result.get_attribute('value')

# sleep(2)
# driver.quit()

# -*- coding: utf-8 -*-

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep

# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get('http://sahitest.com/demo/dragDropMooTools.htm')

# dragger = driver.find_element_by_id('dragger')  # 被拖拽元素
# item1 = driver.find_element_by_xpath('//div[text()="Item 1"]')  # 目标元素1
# item2 = driver.find_element_by_xpath('//div[text()="Item 2"]')  # 目标2
# item3 = driver.find_element_by_xpath('//div[text()="Item 3"]')  # 目标3
# item4 = driver.find_element_by_xpath('//div[text()="Item 4"]')  # 目标4

# action = ActionChains(driver)
# action.drag_and_drop(dragger, item1).perform()  # 1.移动dragger到目标1
# sleep(2)
# action.click_and_hold(dragger).release(item2).perform()  # 2.效果与上句相同，也能起到移动效果
# sleep(2)
# action.click_and_hold(dragger).move_to_element(
#     item3).release().perform()  # 3.效果与上两句相同，也能起到移动的效果
# sleep(2)
# # action.drag_and_drop_by_offset(dragger, 400, 150).perform()  # 4.移动到指定坐标
# action.click_and_hold(dragger).move_by_offset(
#     400, 150).release().perform()  # 5.与上一句相同，移动到指定坐标
# sleep(2)
# driver.quit()


# coding=utf-8
# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from time import sleep

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get('http://sahitest.com/demo/alertTest.htm')

# driver.find_element_by_name('b1').click()

# a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
# sleep(1)
# print a1.text  # text属性输出alert的文本
# a1.accept()  # alert“确认”
# sleep(1)

# driver.quit()


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.alert import Alert
# driver = webdriver.Firefox()
# driver.get('http://sahitest.com/demo/confirmTest.htm')
# driver.find_element_by_name('b1').click()
# sleep(1)
# # a1 = driver.switch_to.alert
# # # a1.accept()
# # a1.dismiss()
# a1 = Alert(driver)
# print a1.text
# a1.dismiss()

# sleep(2)
# print driver.find_element_by_name('t1').text()
# driver.quit()


# # coding=utf-8
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.get('http://sahitest.com/demo/promptTest.htm')
# driver.find_element_by_name('b1').click()
# sleep(1)
# a1 = driver.switch_to.alert
# sleep(1)
# a1.send_keys('dfhghadj')
# sleep(1)
# a1.accept()
# print driver.find_element_by_name('t1').get_attribute('value')
# driver.quit()


# # coding=utf-8
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.alert import Alert

# driver = webdriver.Firefox()
# driver.get('http://sahitest.com/demo/index.htm')
# driver.find_element_by_link_text('Window Open Test With Title').click()
# print driver.current_url
# all_handles = driver.window_handles
# for window in all_handles:
#     if window != current_window:
#         driver.switch_to.window(window)
# print driver.title
# driver.close()
# sleep(1)
# driver.switch_to.window(current_window)
# print driver.title
# driver.quit()


# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from time import sleep
# # from selenium.webdriver.common.alert import Alert

# driver = webdriver.Firefox()
# # driver.maximize_window()
# driver.get('http://sahitest.com/demo/index.htm')

# current_window = driver.current_window_handle
# print driver.current_url
# # 获取当前窗口handle name
# driver.find_element_by_link_text('Window Open Test With Title').click()

# all_windows = driver.window_handles  # 获取所有窗口handle name
# # 切换window，如果window不是当前window，则切换到该window
# for window in all_windows:
#     if window != current_window:
#         driver.switch_to.window(window)

# print driver.title  # 打印该页面title
# sleep(1)
# # # driver.close()
# # # 关闭新窗口后切回原窗口，在这里不切回原窗口，是无法操作原窗口元素的，即使你关闭了新窗口
# # driver.switch_to.window(current_window)
# # sleep(2)
# # print driver.title  # 打印原页面title

# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get('file:///D:/checkboxandradio.html')

# # checkbox
# driver.find_element_by_xpath('//input[@value="cv1"]').click()  # click
# driver.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)
# # send space

# # radio
# driver.find_element_by_xpath('//input[@value="rv1"]').send_keys(Keys.SPACE)  # send space
# sleep(1)
# driver.find_element_by_xpath('//input[@value="rv2"]').click()  # click

# sleep(1)
# driver.quit()
# 从上例可以看出我们对这种checkbox和radio，可以通过直接点击或者发送空格的方式达到选中或者反选的目的。


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Firefox()
# driver.get('file:///home/forin/checkandradio.html')
# sleep(1)
# a1 = driver.find_element_by_xpath("//input[@value='cv3']")
# a1.send_keys(Keys.SPACE)
# sleep(2)
# a2 = driver.find_element_by_xpath("//input[@value='cv2']")
# a2.click()
# sleep(2)
# if a1.is_selected():
#     print 'selected!'
# else:
#     print 'not selected!'

# a3 = driver.find_element_by_xpath("//input[@value='rv1']")
# a3.click()
# sleep(2)
# a4 = driver.find_element_by_xpath("//input[@value='rv2']")
# a4.send_keys(Keys.SPACE)

# sleep(2)
# if a3.is_selected():  # 检查某个框是否被选中 element.is_selected()
#     print 'radio is selected!'
# else:
#     print "not yet!"
# driver.quit()

####

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Firefox()
# driver.get('http://sahitest.com/demo/selectTest.htm')

# s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select

# s1.select_by_index(1)  # 选择第二项选项：o1
# s1.select_by_value("o2")  # 选择value="o2"的项
# s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本

# driver.quit()


# #以上是三种选择下拉框的方式，注意：

# #index从 0 开始
# #value是option标签的一个属性值，并不是显示在下拉框中的值
# #visible_text是在option标签中间的值，是显示在下拉框的值

#
