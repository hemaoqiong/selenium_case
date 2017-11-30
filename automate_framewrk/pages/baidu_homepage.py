# coding=utf-8
from package.common.basepage import BasePage


class Homepage(BasePage):
    # 页面元素
    input_loc = ("id", "kw")
    button_loc = ("id", "su")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页

    def open(self, url):
        # 调用page中的_open打开连接
        self.open(url)
    # 输入要搜索的内容

    def input_keys(self, text):
        self.send_keys(input_keys, text)

    def submmit(self):
        self.click(button_loc)
