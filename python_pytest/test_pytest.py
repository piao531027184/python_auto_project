import unittest
import pytest
import requests
import json
import allure


def setup_module():
    print("模块化开始")


def setup_function():
    print("测试类外的方法开始")


def begin():
    print("测试类外的方法")


def teardown_function():
    print("测试类外的方法结束")


class HttpRequest():

    def __init__(self, method, url, headers, data):
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data

    def http_request(self):
        response = requests.request(self.method, self.url, headers=self.headers, params=self.data)
        response.encoding = response.apparent_encoding
        # print(response.text)
        return response.json()


method2 = "GET"
url2 = "http://apis.juhe.cn/xzpd/query"
headers2 = {}


@allure.feature("发送接口请求验证功能")  # feature定义功能
class TestClass:

    def setup_class(self):
        print("测试类开始")

    def setup(self):
        print("测试方法开始")

    def teardown(self):
        print("测试方法结束")

    def teardown_class(self):
        print("测试类结束")

    @allure.story("手机号为天津，测试成功")
    @pytest.mark.SingleSuccess  # pytest.mark标记分组1
    def test_HttpRequest1(self):
        payload2 = {"men": "天蝎", "women": "水瓶", "key": "96959c42b64970dafb40867ee3e78a4a"}
        test1 = HttpRequest(method2, url2, headers2, payload2)
        result1 = test1.http_request()
        assert "50" == result1["result"]["zhishu"]  # 断言
        print("测试1结束")

    @allure.story("手机号为北京，测试失败")
    @pytest.mark.SingleFail  # pytest.mark标记分组2
    def test_HttpRequest2(self):
        payload2 = {"men": "天蝎", "women": "双鱼", "key": "96959c42b64970dafb40867ee3e78a4a"}
        test2 = HttpRequest(method2, url2, headers2, payload2)
        result2 = test2.http_request()
        assert "60" == result2["result"]["zhishu"]  # 断言
        print("测试2结束")

    @allure.story("参数化测试，测试成功")
    @pytest.mark.SingleSuccess
    @pytest.mark.parametrize("input1,input2,expected", [  # pytest.mark.parametrize参数化
        ('天蝎', '水瓶', '60'),
        ('天蝎', '水瓶', '50')
    ])
    def test_HttpRequest3_parameter(self, input1, input2, expected):
        payload3 = {"men": input1, "women": input2, "key": "96959c42b64970dafb40867ee3e78a4a"}
        test3 = HttpRequest(method2, url2, headers2, payload3)
        result3 = test3.http_request()
        # assert expected == result3["result"]["zhishu"]
        pytest.assume(expected == result3["result"]["zhishu"])
        print("测试3结束")


def teardown_module():
    print("模块化结束")


if __name__ == "__main__":
    pytest.main()
    # pytest.main(["D:/PythonWork/python/test_InterfaceAuto.py",'-m','SingleSuccess'])

'''
#unittest方式：

method  = "POST"
url = "http://test.lemonban.com/ningmengban/mvc/user/login.json"
payload = "{\r\n    \"username\": \"pjl\",\r\n    \"password\": \"619\"\r\n}"
headers = {
  'Content-Type': 'text/plain'
}

# res1 = HttpRequest(method,url,payload,headers)
# res1.http_request()

#1.写测试用例 TestCase
#2.执行测试用例 TextTestRunner
#3.对比实际与期望 断言
#4.测试报告 HtmlReport

#unittest测试类的形式
#创建类，继承测试类的测试用例
class TestMethod(unittest.TestCase):

    #超继承，既有自己的新特性，又继承父类的特性
    def __init__(self,methodName,expected):
        #super(TestMethod,self).__init__(methodName)
        unittest.TestCase.__init__(self,methodName)
        self.expected = expected

    #写测试用例，必须是test_开头
    def test_HttpRequest1(self):
        payload1 = "{\r\n    \"username\": \"zxy\",\r\n    \"password\": \"123456\"\r\n}"
        test1 = HttpRequest(method,url,payload1,headers)
        result1 = test1.http_request()
        self.assertEqual("该手机号没有注册",json.loads(result1)["message"])  #断言
        print("测试1结束")

    def test_HttpRequest2(self):
        payload2 = "{\r\n    \"username\": \"maze\",\r\n    \"password\": \"000000\"\r\n}"
        test2 = HttpRequest(method,url,payload2,headers)
        result2 = test2.http_request()
        self.assertEqual("111111111111",json.loads(result2)["message"])
        print("测试2结束")

    #参数化
    def test_HttpRequest3(self):
        payload3=''
        test3 = HttpRequest(method,url,payload3,headers)
        result3 = test3.http_request()
        self.assertEqual(self.expected,json.loads(result3)["message"])

'''
