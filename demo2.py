# coding=utf-8

# example1

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
# print 'url:', driver.current_url
# driver.find_element_by_id('kw').send_keys('selemium')

# aa = driver.find_element_by_id('su')
# aa.click()
# sleep(2)
# print 'now_url:', driver.current_url

# # print aa.get_attribute('name')


# driver.back()
# print 'back_url:', driver.current_url
# driver.forward()
# print "go to", driver.current_url
# driver.refresh()
# print 'refren_url', driver.current_url
# driver.quit()
# driver.scoll()
# (window).scrollTop(300)
# driver.scrollTop()


# example2

# driver.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20141108-1/')
# driver.switch_to.frame('iframe')
# js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"
# driver.execute_script(js)
# driver.find_element_by_id('txtBeginDate').send_keys('2019-09-16')
# sleep(2)
# print driver.find_element_by_id('txtBeginDate').get_attribute('value')
# driver.quit()


# example3 关闭窗口close与quit
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.get('http://sahitest.com/demo/index.htm')
# sleep(2)
# aa = driver.get_window_position()
# print driver.current_window_handle
# print aa  # 查看当前window handle

# driver.find_element_by_link_text('Window Open Test').click()
# sleep(2)  # 打开新window1

# driver.find_element_by_link_text(
#     'Window Open Test With Title').click()  # 打开新window2
# sleep(2)
# print driver.window_handles
# # 查看所有window handles
# driver.close()
# sleep(2)

# print driver.window_handles
# # 查看现在的所有window handles，可看到只是关闭了最开始的一个window，其他两个window还在

# driver.quit()  # 看到所有window都被关闭


# example ActionChains方法列表fa
from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('http://sahitest.com/demo/clicks.htm')

# driver.find_element_by_xpath('//input[@value="click me"]')
# driver.find_element_by_xpath('//input[@value="dbl click me]').double_click()
# driver.find_element_by_xpath('/html/body/form/input[4]').context_click()
double_click = driver.find_element_by_xpath('//input[@value="dbl click me"]')
# right_click = driver.find_element_by_xpath('/html/body/form/input[4]')


actions = ActionChains(driver)

actions.move_to_element(double_click).double_click()
# actions.double_click()
# sleep(2)
# # anctions.click()
# actions.double_click()
# sleep(2)

# ActionChains(driver).move_to_element()click(single_click).perform()
# ActionChains(driver).move_to_element(single_click).click().perform()
# ActionChains(driver).click(single_click).
# double_click).context_click(right_click).perform()  # 链式用法

# sleep(2)
# ActionChains(driver).double_click(double_click).perform()
sleep(2)
# ActionChains(driver).context_click(right_click).perform()
# driver.quit()
