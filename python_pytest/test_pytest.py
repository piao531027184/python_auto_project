import pytest
import requests
import allure
import yaml


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


@allure.feature("发送接口请求验证功能")  # allure.feature('功能名称'):标注功能名称
class TestClass:

    def setup_class(self):
        print("测试类开始")

    def setup(self):
        print("测试方法开始")

    def teardown(self):
        print("测试方法结束")

    def teardown_class(self):
        print("测试类结束")

    url = "http://www.qq.com"

    @allure.testcase(url, 'qq首页')  # 加入链接
    @allure.story("测试成功")  # allure.story('子功能名称'):标注子功能名称
    @pytest.mark.SingleSuccess  # pytest.mark标记分组
    @pytest.mark.run(order=3)
    def test_HttpRequest1(self):
        payload2 = {"men": "天蝎", "women": "水瓶", "key": "96959c42b64970dafb40867ee3e78a4a"}
        with allure.step("打印请求参数:"):  # allure.step('步骤'):标注步骤
            print(payload2)
        test1 = HttpRequest(method2, url2, headers2, payload2)
        result1 = test1.http_request()
        with allure.step("打印响应:"):
            print(result1)
        assert "50" == result1["result"]["zhishu"]  # 断言
        allure.attach.file("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)  # 添加纯文本
        print("测试1结束")

    # --allure-link-pattern=issue:http://www.sina.com/issue/{}
    # 执行的时候复制上面的信息:
    # pytest test_pytest.py --allure-link-pattern=issue:http://www.sina.com/issue/{} --alluredir report/allure_raw
    @allure.issue('140', '这是一个issue')  # 添加失败的链接
    @allure.story("测试失败")
    @allure.severity(allure.severity_level.TRIVIAL)  # 标记分类
    @pytest.mark.SingleFail  # pytest.mark标记分组2
    @pytest.mark.run(order=1)  # 指定执行顺序
    #  @pytest.mark.skip("此次测试不执行")  # 跳过该测试用例
    # @pytest.mark.xfail                       #标注该失败的用例结果为pass
    def test_HttpRequest2(self):
        payload2 = {"men": "天蝎", "women": "双鱼", "key": "96959c42b64970dafb40867ee3e78a4a"}
        test2 = HttpRequest(method2, url2, headers2, payload2)
        result2 = test2.http_request()
        assert "60" == result2["result"]["zhishu"]  # 断言
        allure.attach.file("<body>这是一段HTML代码块</body>", "HTML代码块", attachment_type=allure.attachment_type.HTML)  # 添加HTML
        print("测试2结束")

    @allure.story("参数化测试，测试成功")
    @allure.link("http://www.baidu.com", name="百度首页")  # 加入链接
    @pytest.mark.SingleSuccess
    @pytest.mark.run(order=2)
    @allure.severity(allure.severity_level.NORMAL)  # 标记分类
    @pytest.mark.parametrize(("input1,input2,expected"),
                             yaml.safe_load(open("./data.yaml", encoding="utf-8")))  # YAML文件存储参数化
    # @pytest.mark.parametrize("input1,input2,expected", [  # pytest.mark.parametrize参数化
    #     ('天蝎', '水瓶', '60'),
    #     ('天蝎', '水瓶', '50')
    # ])

    # 参数组合
    # @pytest.mark.parametrize("input1", ['天蝎','白羊','巨蟹'])
    # @pytest.mark.parametrize("input2", ['水瓶', '双鱼'])
    # @pytest.mark.parametrize("expected", ['50', '60'])

    def test_HttpRequest3_parameter(self, input1, input2, expected):
        payload3 = {"men": input1, "women": input2, "key": "96959c42b64970dafb40867ee3e78a4a"}
        test3 = HttpRequest(method2, url2, headers2, payload3)
        result3 = test3.http_request()
        # assert expected == result3["result"]["zhishu"]
        pytest.assume(expected == result3["result"]["zhishu"])
        allure.attach.file("C:/Users/朴建霖/Desktop/新建文件夹/晓宇证件照.jpg", name="这是一个图片",
                           attachment_type=allure.attachment_type.JPG)
        print("测试3结束")


def teardown_module():
    print("模块化结束")


if __name__ == "__main__":
    pytest.main()
    # pytest.main(["D:/PythonWork/python/test_InterfaceAuto.py", '-m', 'SingleSuccess'])
