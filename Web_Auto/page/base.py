from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 定义类变量
    _base_url = "http://172.16.60.131/user/login"

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self._driver = ""

    def init_driver(self):

        if self.driver is None:
            # 设置浏览器不提供可视化页面
            # option = webdriver.ChromeOptions()
            # option.add_argument('headless')
            # self.driver = webdriver.Chrome(chrome_options=option)
            self._driver = webdriver.Chrome(r"D:\Google\Chrome\Application\chromedriver.exe")

            if self._base_url != "":
                self._driver.get(self._base_url)
                # 设置浏览器窗口最大化
                # self._driver.maximize_window()

        else:

            self._driver = self.driver

        return self._driver

# # 定义异常类
# class ErrorInfo(Exception):
#     @staticmethod
#     def error_msg_fun(error,error_msg_list):
#         error_msg = error+"失败"
#         if error_msg_list[error_msg_list.index(error)+1] != "未测试":
#             for i in range(error_msg_list.index(error)+1,len(error_msg_list)):
#                 error_msg+=error_msg_list[i]+"."
#         return error_msg
