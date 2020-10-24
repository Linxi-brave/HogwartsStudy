
from util.find_element import FindElement
from selenium import webdriver
class SeleniumBasedriver(object):
    def __init__(self,url):
        self.option = webdriver.ChromeOptions()

        # 禁用JavaScript
        self.option.add_argument("--disable-javascript")
        # 谷歌文档提到需要加上这个属性来规避bug
        self.option.add_argument('--disable-gpu')
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
        self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)
        # self.url = "https://inv.mxcloud.work/login"
        self.url = url
        self.driver.get(self.url)
        self.driver.maximize_window()

        # self.getElement = FindElement(driver=self.driver)
        self.driver.implicitly_wait(3)

    def get_driver(self):
        self.driver = self.driver
        return self.driver

