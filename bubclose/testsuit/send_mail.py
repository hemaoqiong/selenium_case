# coding=utf-8

from basepage import *
from selenium.webdriver.common.by import By


class send_mail(BasePage):
    # 发送按钮
    # 收件人
    reciver_loc = (By.CLASS, 'nui-editableAddr-ipt')
# 主题
    object_loc = (By.CLASS, 'nui-ipt-input')
# 输入框
# 底部发送按钮
# 顶部发送按钮
