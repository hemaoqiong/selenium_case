# coding=utf-8
# coding=utf-8
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select

#from selenium.common.exceptions import NameError
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('https://www.taobao.com/')
driver.find_element_by_class_name("h").click()
time.sleep(3)
driver.find_element_by_id('J_Quick2Static').click()
# driver.find_elements_by_class_name('login-links').click()
# driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/i[2]').click()
time.sleep(4)
driver.find_element_by_id('TPL_username_1').send_keys(u'何茂琼2014')
driver.find_element_by_id('TPL_password_1').send_keys('hemaoqiong123')
driver.find_element_by_id('J_SubmitStatic').click()
time.sleep(3)
now_user = driver.find_element_by_class_name('site-nav-login-info-nick')

# now_user = driver.find_element_by_xpath(
#   '//div[1]/div/ul[1]/li[1]/div[1]/div[2]/a[1]')
# if now_user == u'何茂琼2014':
# print '登录成功'
# else:
#raise NameError('user name error！')
# driver.find_element_by_class_name('site-nav-pipe')
aa = driver.find_element_by_link_text('何茂琼2014')
bb = driver.find_element_by_class_name('site-nav-pipe')
ActionChains(driver).move_to_element(bb).perform()
time.sleep(2)
driver.find_element_by_class_name('site-nav-pipe').click()


# driver.quit()
