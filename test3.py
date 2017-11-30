# coding=utf-8
# from selenium import webdriver
# from time import sleep

# # driver = webdriver.Firefox()

# 例子1
# driver.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20150325-1')
# driver.switch_to.frame('iframe')
# sleep(3)
# driver.maximize_window()
# driver.find_element_by_id('message1').send_keys('Hello world')
# sleep(3)
# driver.find_element_by_id('message2').send_keys('value')
# # print driver.find_element_by_id('message1').get_attribute('value')
# print driver.find_element_by_id('message1').get_attribute('message1')


# driver.get('http://ueditor.baidu.com/website/examples/completeDemo.html')
# driver.switch_to.frame('ueditor_0')
# sleep(3)
# sting = 'hello,world!hello helldsgoafdjgjsdjjsgjfkfjgkfdksk'
# driver.find_element_by_tag_name('body').send_keys(sting)
# print driver.find_element_by_tag_name('body').text
# sleep(2)
# driver.quit()

# example2:
# from selenium import webdriver
# from time import sleep

# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.dir', 'd:\\')
# profile.set_preference('browser.download.folderList', 2)
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference(
#     'browser.helperApps.neverAsk.saveToDisk', 'application/zip')

# driver = webdriver.Firefox(firefox_profile=profile)

# driver.get('http://sahitest.com/demo/saveAs.htm')
# # driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
# driver.find_element_by_xpath('//a[1]').click()

# sleep(3)
# driver.quit()
from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.wait import webDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://huilansame.github.io')
locator = (By.LINK_TEXT, 'CSDN')

try:
    WebDriverWait(driver, 20, 0.5).until(
        EC.presence_of_element_located(locator))
    print driver.find_element_by_link_text('CSDN').get_attribute('href')
finally:
    driver.close()
# sleep(2)

# driver.maximize_window()

# print driver.current_url
# driver.quit()
