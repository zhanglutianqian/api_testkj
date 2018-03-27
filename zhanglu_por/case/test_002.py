# _*_coding:UTF-8_*_

# ------------------------------------------------------
# oeasy
# 2018/3/23  9:56 
# ------------------------------------------------------
import requests
import unittest

class Test1(unittest.TestCase):
    u'''铜仁项目首页测试0001接口'''

    @classmethod
    def setUpClass(cls):
        print("setUpClass初始化操作：用例开始前只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass收尾清理操作：用例结束时候只执行一次")

    def setUp(self):
        self.s = requests.session()

        # url1 = "http://192.168.20.36:8089/portal/account/getAccountByToken.do"
        # r1 = self.s.get(url1)
        # print(r1.text)
        # print(r1.cookies)

        c = requests.cookies.RequestsCookieJar()
        c.set("JSESSIONID", "AFBF34903DED4BD5DEB975FF3BD4C331")
        c.set("TOKEN", "256999ebc6a456b99f3315241a75be36_1087885c1945473ca0f3825a048b69b6")
        self.s.cookies.update(c)
    def tearDown(self):
        pass

    def test_01(self):

        r3 = self.s.get("http://192.168.20.36:8089/portal/speicalPerson/queryByCategory.do?province_code=520000&city_code=520600")
        print(r3.text)
        print(r3.cookies)
        print(type(r3.text))
        # a = r3.json()
        # b = a["msg"]
        # self.assertIn(u"", b)
        # print(b)

if __name__ == "__main__":
    unittest.main()