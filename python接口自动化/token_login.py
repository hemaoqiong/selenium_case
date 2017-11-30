# coding=utf-8

import requests
# body = {'Content-Disposition: form-data; name="grant_type"': 'password',
#         'Content-Disposition: form-data; name="scope"': 'ui',
#         'Content-Disposition: form-data; name="classType"': '1',
#         'Content-Disposition: form-data; name="username"': 'admin',
#         'Content-Disposition: form-data; name="password"': '123456'}
'''上注释的直接从抓包工具中复制过来的不对，修改后正常'''

body = {'grant_type': 'password',
        'scope': 'ui',
        'classType': '1',
        'username': 'admin',
        'password': '123456'}

#  登录抓包获取的头部
headers1 = {'Connection': 'keep-alive',
            'Content-Length': '541',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400',
            'authorization': 'Basic YnJvd3Nlcjo = ',
            'content - type': 'multipart / form - data;boundary = ----WebKitFormBoundaryxDH3jfRYiqrLYBBn',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'}

url1 = 'http://60.205.169.195:4001/api/account/oauth/token'  # 找带token网址
s = requests.session()
# r = s.get(url, headers=headers)
r1 = s.post(url1, data=body, headers=headers1)
print r1.status_code
# 这里token在返回的json里，可以直接提取
print r1.json()
print 'ouput token!!!!!'
token = r1.json()["refresh_token"]
print token

# end
