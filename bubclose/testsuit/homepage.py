# coding=utf-8
from basepage import *
from selenium.webdriver.common.by import By


class Homepage126(BasePage):

    # def __init__(self):
    #     driver = webdiver.firefox()
    # top page location

    cp_loc = (By.LINK_TEXT, u"邮箱黄页")
    cp_email_loc = (By.LINK_TEXT, u'企业邮箱')
    vip_email_loc = (By.LINK_TEXT, u'VIP邮箱')
    fuser_login_loc = (By.LINK_TEXT, u'国外用户登录')
    app_loc = (By.LINK_TEXT, u'手机客户端')
    help_loc = (By.LINK_TEXT, u'帮助')
    prob_loc = (By.LINK_TEXT, u'常见问题')
# The buttom of page location
    homepage_loc = (By.LINK_TEXT, u'网易首页')
    about_loc = (By.LINK_TEXT, u'关于网易免费邮')
    made_loc = (By.LINK_TEXT, u'网易智造')
    monney_loc = (By.LINK_TEXT, u'网易•有钱')
    select_loc = (By.LINK_TEXT, u'网易严选')
    together_loc = (By.LINK_TEXT, u'网易一起拼')
    # advertisement location
    ad_lick_loc = (By.ID, 'theme')
    ad_next_loc = (By.ID, 'nextTheme')
    ad_Previous_loc = (By.ID, 'prevTheme')

    # click 邮箱黄页

    def click_cppage(self):
        self.click(self.cp_loc)  # must add self befor element

    # click企业邮箱

    def click_cpemail(self):
        self.click(self.cp_email_loc)  # 元素前必须加self，不然报错
    # click VIP邮箱

    def click_vip(self):
        self.click(vip_email_loc)
    # click国外用户登录

    def click_fuser(self):
        self.click(fuser_login_loc)

    def click_ad(self):
        self.find_element(self.ad_lick_loc).click()
