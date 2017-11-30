
# requests方法使用

# coding:utf-8
import requests

__author__ = 'harmo'


def get_demo():
    """
    requests 的get方法演示,不带参数
    by:Harmo
    :return:
    """
    url = 'http://www.baidu.com'
    res = requests.get(url)
    print res.url
    print res.status_code

    aa = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post('http://httpbin.org/post', data=aa)
    print(r.text)


if __name__ == '__main__':
    get_demo()
# 运行结果
# http://www.baidu.com/
# 200
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "23",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.7.0 CPython/2.7.6 Linux/4.2.0-41-generic"
#   },
#   "json": null,
#   "origin": "171.217.34.250",
#   "url": "http://httpbin.org/post"
# }


# ##### 对一个用户登录的接口进行测试

def test_admin_user_login(self):
    """
    测试用户登录
    by:Harmo
    :return:
    """

    url = "%s%s" % (self.base_url, '/task/admin-user-login/')

    params = dict(
        user='admin',
        password='222222',

    )

    res = requests.post(url, data=params)
    print res.text

    res_dict = json.loads(res.text)
    self.assertEqual(res_dict['code'], 200)
