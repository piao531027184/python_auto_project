import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Action:
    def __init__(self, driver):
        self.driver = driver

    # 报错截图并上传到allure
    def error_screen(self):
        now_time = time.strftime("%Y$m$d.%H.%M.%S")
        screen = self.driver.get_screenshot_as_file("{}.jpg".format(now_time))
        allure.attach("报错截图", screen, allure.attachment_type.PNG)

    # 定义查找元素函数，只需传元素定位参数
    def find(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    # 定义鼠标悬停
    def hover(self, locator):
        return ActionChains(self.driver).move_to_element(self.driver.find_element(By.CSS_SELECTOR, locator)).perform()
