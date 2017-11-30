# coding=utf-8
from basepage import *
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    QR_code = (By.ID, 'lbApp')     # 点击“二维码登陆”
    load_mail = (By.LINK_TEXT, u'下载邮箱大师')   # 点击“下载邮箱大师”
    login = (By.ID, 'lbNormal')  # 点击“邮箱账号登陆”
    login_name = (By.NAME, 'email')  # input:邮箱帐号或手机号，因id是动态的，所以用name定位
    login_pw = (By.NAME, 'password')    # input:密码
    ten_login = (By.ID, 'un-login')                 # 十天免登陆
    fg_pw = (By.ID, 'auto-id-1508813090595')        # 忘记密码按钮
    login_button = (By.ID, 'dologin')               # 登陆按钮
    register_button = (By.ID, 'changepage')            # 注册按钮
    spn_loc = (By.ID, 'nerror')  # 用户名或密码不合理是Tip框内容展示
    login_frame = (By.ID, 'x-URS-iframe')
    # '''
    # LOGIN_URL='http://www.126.com/
    # ''''

    def QR_code(self):
        self.click(self.QR_code)    # 点击“二维码登陆”,调用page类的click()

    def load_mail(self):
        self.click(self.load_mail)  # 点击“下载邮箱大师”

    def normal_login(self):
        self.click(self.login)      # 点击“邮箱账号登陆”

    def input_username(self, username):
        self.find_element(self.login_name).send_keys(
            username)  # 调用send_keys方法，输入用户名

    def input_password(self, password):
        self.send_keys(self.login_pw, password)  # 调用send_keys方法，输入密码

    def click_tenlg(self):
        self.click(self.ten_login)  # 调用click方法，点击十天免登陆

    def click_forgetpw(self):
        self.click(self.fg_pw)         # 忘记密码按钮

    def click_login(self):
        self.click(self.login_button)    # click登陆按钮

    def click_register(self):
        self.click(self.register_button)   # 注册按钮
