


from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    # 基类 ： 实现最基本的方法，driver 实例化，find() 等
    driver: WebDriver
    url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def __init__(self,driver:WebDriver):

        if driver == None:
            self.option = webdriver.ChromeOptions()

            self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'

            self.option.add_experimental_option('w3c', False)
            self.option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            self.driver = webdriver.Chrome(options=self.option, executable_path=self.path)

            self.driver.implicitly_wait(2)
            self.driver.maximize_window()
        else :
            self.driver = driver

        if self.url != '':
            self.driver.get(self.url)

    def find(self,by,locator):
        '''
        封装查找元素
        :return: 返回元素
        '''
        return self.driver.find_element(by,locator)

    def finds(self,by,locator):

        return self.driver.find_elements(by,locator)

    def wait_for_click(self,locator,timeout = 10):
        '''
        判断元素是否可点击，可点击则返回元素
        '''
        element:WebElement =  WebDriverWait(self.driver,timeout).until(
            expected_conditions.element_to_be_clickable(locator))

        return element

