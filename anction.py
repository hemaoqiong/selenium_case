# coding=utf-8
'''方法1'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import UnexpectedAlertPresentException
# from time import sleep

# driver = webdriver.Chrome()
# driver.get("https://www.helloweba.com/demo/2017/unlock/")


# dragger = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]

# action = ActionChains(driver)

# action.click_and_hold(dragger).perform()  # 鼠标左键按下不放

# for index in range(200):
#     try:
#         action.move_by_offset(2, 0).perform()  # 平行移动鼠标
#     except UnexpectedAlertPresentException:
#         break
#     action.reset_actions()
#     sleep(0.1)  # 等待停顿时间


# # 打印警告框提示
# success_text = driver.switch_to.alert.text
# print(success_text)

# sleep(5)

# driver.quit()

''' 方法2  '''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/demo/2017/unlock/")
sleep(2)
dragger = driver.find_elements_by_class_name('slide-to-unlock-handle')[0]
actions = ActionChains(driver)
# actions.click_and_hold(dragger)
for index in range(100):
    try:
        actions.drag_and_drop_by_offset(dragger, 500, 0).perform()
        # 将移动的横坐标设置很大，大于滑动边框的距离，使用drag_and_drop直接移动
    except UnexpectedAlertPresentException:
        break


text1 = driver.switch_to.alert.text
print(text1)
driver.quit()
