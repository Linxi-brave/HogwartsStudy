from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):

        pass

    # 进入到注册页
    def goto_register(self):

        self.driver.find_element()

        pass