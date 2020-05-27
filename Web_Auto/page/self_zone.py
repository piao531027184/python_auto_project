from Web_Auto.page.action import Action


class Self_zone(Action):
    # “新建”按钮
    create_file = "#create-file"
    # 选择新建“文件夹”
    choose_file = "ul[class~='create-dropdown'] > div > li > span > svg[class~='folder']"
    # 名称输入框
    fileName_slug = "#new-file > div > div > input"
    # 输入框确认按钮
    fileName_submit = "#new-file > div > div > span > span:nth-child(1) > svg"
    # 进入个人空间按钮
    self_zone = "#page-left > div.sub-menu > div.menu-item.m-self-zone > a > span"
    # 创建的文件夹名
    foder_name = "UI自动化"

    # 创建文件/文件夹
    def create_folder(self):
        self.find(self.self_zone).click()
        self.find(self.create_file).click()
        self.find(self.choose_file).click()
        self.find(self.fileName_slug).send_keys(self.foder_name)
        self.find(self.fileName_submit).click()

    # 点击创建的文件夹
    def click_folder(self):
        self.find(self.choose_file).click()
