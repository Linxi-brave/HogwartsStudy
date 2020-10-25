from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class RegisterPage():

    '''
    def __init__(self,driver:WebDriver):
    可以给对象完成类型的指定，对象就可以有这个类型，那么就可以调用对应的方法
    只针对 pycharm IDE
    '''
    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 注册信息
    def register(self):
        self.driver.get_element(By.ID,"").send_keys("aaa")
        self.driver.get_element(By.Id,"").send_keys("bbbb")
        self.driver.get_element(By.ID,"").send_keys("sss")
        self.driver.get_element(By.ID,"").click()
        return True
