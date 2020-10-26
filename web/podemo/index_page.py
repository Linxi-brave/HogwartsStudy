from selenium.webdriver.chrome import webdriver

from web.podemo.login_page import LoginPage


class IndexPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("")

        '''
        PO 实现的六大原则：
        1、公共方法代表了页面的服务
        2、不要暴露页面的内部细节
        3、不要在界面对象添加断言
        4、方法return了其他PO 对象
        5、不要封装不需要的服务
        6、相同行为产生不同的结果，需要不同的方法
        '''

     # 进入登录界面
    def go_register(self):
        # 点击登录
        self.driver.get_element().click()
        # 返回登录界面
        return  LoginPage(self.driver)