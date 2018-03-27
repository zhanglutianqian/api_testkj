# _*_coding:UTF-8_*_

# ------------------------------------------------------
# oeasy
# 2018/3/22  17:55 
# ------------------------------------------------------

import requests
import unittest

class Test1(unittest.TestCase):
    u'''铜仁项目登录测试'''

    @classmethod
    def setUpClass(cls):
        print("setUpClass初始化操作：用例开始前只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass收尾清理操作：用例结束时候只执行一次")

    def setUp(self):
        self.url = "http://192.168.20.36:8089/portal/account/login.do"

    def tearDown(self):
        pass

    def test_01(self):
        body = {"account": "zhanglu",
                "password": "353e01a16b0dfcb055e7f74921565a3a9770c67a3e2a293509c0d36bc5ba70c7f67a06e72f46d0b24c0481828a"
                            "a6d2b235fdc0f97bbb5db2c6844d40a74abb18a875a5b50b14b467059a7cab52771226f686a6292fa2ecf82f5a"
                            "4e41bafd6f4ee962daa6c8c010433a673a7e823a8f3b7f67b3c1808449292ba3bc050af2afed",
                "verificationcode": "123456"}

        r = requests.post(self.url, data=body)
        a = r.json()
        b = a["msg"]
        self.assertIn(u"登录失败", b)
        print(b)
    def test_02(self):
        body = {"account": "",
                "password": "353e01a16b0dfcb055e7f74921565a3a9770c67a3e2a293509c0d36bc5ba70c7f67a06e72f46d0b24c0481828a"
                            "a6d2b235fdc0f97bbb5db2c6844d40a74abb18a875a5b50b14b467059a7cab52771226f686a6292fa2ecf82f5a"
                            "4e41bafd6f4ee962daa6c8c010433a673a7e823a8f3b7f67b3c1808449292ba3bc050af2afed",
                "verificationcode": "123456"}

        r = requests.post(self.url, data=body)
        a = r.json()
        b = a["msg"]
        self.assertIn(u"登录失败", b)
        print(b)
    def test_03(self):
        body = {"account": "zhanglu",
                "password": "",
                "verificationcode": "123456"}

        r = requests.post(self.url, data=body)
        a = r.json()
        b = a["msg"]
        self.assertIn(u"登录失败", b)
        print(b)

if __name__ == "__main__":
    unittest.main()