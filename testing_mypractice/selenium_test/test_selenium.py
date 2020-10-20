
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium():
    def setup_class(self):
        self.option = webdriver.ChromeOptions()

        # 禁用JavaScript
        self.option.add_argument("--disable-javascript")
        # 谷歌文档提到需要加上这个属性来规避bug
        self.option.add_argument('--disable-gpu')
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
        self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)

        self.driver.implicitly_wait(3)
        self.driver.get("https://home.bitkinetic.com/board/time_collect")
        self.driver.maximize_window()
    def setup(self):
        pass
    def teardown(self):
        pass


    def test_sleep(self):
        sleep(2)
        self.driver.implicitly_wait(2)
        # WebDriverWait(self.driver).until()

    # def test_wait(self):
    #
    #     def wait(x):
    #         return self.driver.find_element(Element)
    #     WebDriverWait(self.driver).until(wait)
    #     # # 元素可被点击
    #     # expected_conditions.invisibility_of_element(Element)
    #
    #     WebDriverWait(self.driver).until(expected_conditions.invisibility_of_element(Element))
    #
    #
