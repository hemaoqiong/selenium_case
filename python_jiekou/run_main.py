# coding=utf-8
import os
import unittest
# curl_path=os.path.dirname(os.path.abspath(__file__))
curl_path = os.path.dirname(os.path.abspath("run_main.py"))
curl_path2 = os.path.abspath("run_main.py")
# curl_path:/home/forin/WorkSpace/python_jiekou   第一个输chu路径
# curl_path2:/home/forin/WorkSpace/python_jiekou/run_main.py  第二个为绝对路径，带文件名的
print curl_path
print curl_path2


def add_case(rule=test * .py)
    case_path = os.path.join(curl_path, "case")  # 用例文件夹
    if not os.path.exists(case_path):     # 如果不存在“case”文件夹，自动创建一
    os.mikdir(case_path)

    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule top_level_dir=None)
    # rule="test*.py"这个是匹配用例脚本名称的规则，默认匹配test开头的所有用例
    print discover
    return discover
