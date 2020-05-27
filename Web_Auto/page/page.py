import time

import allure
from selenium.webdriver.common.by import By

from Web_Auto.page.Auth_management import Auth_management
from Web_Auto.page.link_management import Link_management
from Web_Auto.page.login import Login
from Web_Auto.page.management_console import Management_console
from Web_Auto.page.message import Message
from Web_Auto.page.my_approval import My_approval
from Web_Auto.page.my_favorite import My_favorite
from Web_Auto.page.recent_view import Recent_view
from Web_Auto.page.self_zone import Self_zone
from Web_Auto.page.trash import Trash
from Web_Auto.page.user_settings import User_settings


class Page:

    def __init__(self, driver):
        self.driver = driver

    # 进入登录页
    def login_page(self):
        return Login(self.driver)

    # 进入个人空间
    def goto_self_zone(self):
        return Self_zone(self.driver)

    # 进入最近访问
    def goto_recent(self):
        return Recent_view(self.driver)

    # 进入我的收藏
    def goto_favorite(self):
        return My_favorite(self.driver)

    # 进入回收站
    def goto_trash(self):
        return Trash(self.driver)

    # 进入链接管理
    def goto_link_management(self):
        return Link_management(self.driver)

    # 进入我的审批
    def goto_my_approval(self):
        return My_approval(self.driver)

    # 进入授权管理
    def goto_auth_managemeng(self):
        return Auth_management(self.driver)

    # 进入管理控制台
    def goto_managament_console(self):
        return Management_console(self.driver)

    # 进入消息
    def goto_message(self):
        return Message(self.driver)

    # 打开用户设置窗口
    def open_user_settings(self):
        return User_settings(self.driver)

    # 报错截图并上传到allure
    def error_screen(self):
        now_time = time.strftime("%Y$m$d.%H.%M.%S")
        screen = self.driver.get_screenshot_as_file("{}.jpg".format(now_time))
        allure.attach("报错截图", screen, allure.attachment_type.PNG)

    # 定义查找元素函数，只需传元素定位参数
    def find(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)
