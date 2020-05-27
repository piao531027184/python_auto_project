from Web_Auto.page.action import Action
from Web_Auto.page.home_page import Home_page


class Login(Action):
    # 继承BasePage,重写类变量
    # _base_url = "http://172.16.60.131/user/login"

    # 用户名改密
    username = "admin"
    passwrod = "123456"

    # 域用户登录勾选框
    auto_domain = "#auto_domain"
    # 用户名输入框
    user_slug = "#user_slug"
    # 密码输入框
    pass_slug = "#pwd"
    # 登录按钮
    submit_button = "#submit_button"
    # 下次自动登录勾选框
    auto_login = "#auto_login"
    # 英文切换按钮
    switch_en = "#lang"

    # 登录并进入首页（企业空间）
    def login(self):
        self.find(self.auto_domain).click()
        self.find(self.user_slug).send_keys(self.username)
        self.find(self.pass_slug).send_keys(self.passwrod)
        self.find(self.submit_button).click()
