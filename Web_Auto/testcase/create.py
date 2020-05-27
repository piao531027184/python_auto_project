from Web_Auto.page.base import BasePage
from Web_Auto.page.page import Page


class Test_create:

    def setup(self):

        self.driver = BasePage(driver=None).init_driver()
        self.driver.implicitly_wait(10)
        self.page = Page(self.driver)

    def test_create_folder(self):
        try:
            self.page.login_page().login()
            self.page.goto_self_zone().create_folder()

        except Exception as msg:
            print("出现异常：", msg)
            self.page.error_screen()
            raise

    def teardown(self):
        self.driver.quit()
