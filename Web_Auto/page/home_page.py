from Web_Auto.page.action import Action


class Home_page(Action):
    # “新建”按钮
    create_file = "#create-file"
    # 选择新建“文件夹”
    choose_file = "ul[class~='create-dropdown'] > div > li > span > svg[class~='folder']"
    # 名称输入框
    fileName_slug = "#new-file > div > div > input"
    # 输入框确认按钮
    fileName_submit = "#new-file > div > div > span > span:nth-child(1) > svg"

    # 创建的文件夹名
    foder_name = "测试用文件名12"

    # 创建文件/文件夹
    def create_folder(self):
        self.find(self.create_file).click()
        self.find(self.choose_file).click()
        self.find(self.fileName_slug).send_keys(self.foder_name)
        self.find(self.fileName_submit).click()

    # # 选择并进入文件夹
    # def select_folder(self):
    #     self.find("div[drag-path={foder_name}]").click()

    # # 创建外链
    # def create_link(self):
    #     self.find("")
