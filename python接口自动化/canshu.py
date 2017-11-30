# coding=utf-8
# 接口自动化需要先使用fiddler查看接口参数
# python接口自动化7-参数关联

import requests
import re
# 1.login fist
json = {'input1': 'EoiPA1cNtkcplFs1zuY3BZTDaeJ47Kf2kKwbLJNJbtv2wIKOk05kzaL7rXTrGqFX0RxLRI61Pp9KamPG4j5dvGVGQF7ICEz1K8Mowc76yFu1tnBD9KNjP3Lo+J4xbIP4MHOuasSx5p00aWj+ujGEUHNlFT/Tt5pDtOtuYaLdHlU=',
        'input2': 'nniTaoxESUk18JAAWJFOyh9Mp6N0B2zJJm3+G2Umk/x/CMgfKb4atZ8voHQCP5vi0Pgt1CafGarigFfkbvvTQM6wDFAcGfIUIgby26GUvxVLUA7w9BTv+KHQ20Tl4gF38RLrTySlEuXKmV7ihl3Zvkzk2gng3FfuNZ7cHO6RCfw=',
        'remember': True}

headers = {'Connection': 'keep-alive',
           'Content-Length': 385,
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400',
           'Content-Type': 'application/json; charset=UTF-8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           "Cookie": "__gads=ID=78b65628f617f98a:T=1494556849:S=ALNI_MbWOzoT4vtJhp7zIxN6E8gOa7Po4Q; UM_distinctid=15c760d74a1a-092ed9f25dc6ff-31437652-1fa400-15c760d74a2458; _ga=GA1.2.448265553.1493953194; _gid=GA1.2.1024715553.1501468094; SERVERID=227b087667da6f8e99a1165002db93f6|1501657023|1501655054; Hm_lvt_6279c8b8905ad038e867c96dea646c6a=1501469333,1501657248; Hm_lpvt_6279c8b8905ad038e867c96dea646c6a=1501657364"}

url1 = 'https://passport.cnblogs.com/user/signin'
s = requests.session()  # session登录
r = s.post(url1, json=json, headers=headers, verify=False)
print r.json()
# 预计结果-success=True
# 第二步：保存草稿
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {'__VIEWSTATE': '',
        ' __VIEWSTATEGENERATOR': 'FE27D343',
        'Editor$Edit$txbTitle': 'pathon标题2',
        'Editor$Edit$EditorBody': '<p>接口自动化需要先使用fiddler查看接口参数</p>',
        'Editor$Edit$Advanced$ckbPublished': 'on',
        'Editor$Edit$Advanced$chkDisplayHomePage': 'on',
        'Editor$Edit$Advanced$chkComments': 'on',
        'Editor$Edit$Advanced$chkMainSyndication': 'on',
        'Editor$Edit$lkbDraft': '存为草稿'}
r1 = s.post(url2, data=body, verify=False)
# 获取当前url地址,带有postID,postid=7274446&
print r1.url
# 第三步：正则提取需要的参数值
# import re
pattern = r'postid=(.+?)&'
postid = re.findall(pattern, r1.url)
print postid  # 这里是list
# 提取为字符串
print postid[0]
# 第四步：删除草稿箱
url3 = "https://i.cnblogs.com/post/delete"
json3 = {"postId": postid[0]}
r3 = s.post(url3, json=json3, verify=False)
print r3.json()
