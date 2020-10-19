'''
等待方式可以互相使用
直接等待：time.sleep(1)
隐式等待：全局等待，所有的元素都会进行等待 ，self.driver.implicitly_wait(2)
显示等待：
        from selenium.webdriver.support import expected_conditions
        from selenium.webdriver.support.wait import WebDriverWait
        def wait(x):
            return self.driver.find_element(Element)
        WebDriverWait(self.driver).until(wait)
        # # 元素可被点击
        # expected_conditions.invisibility_of_element(Element)

        WebDriverWait(self.driver).until(expected_conditions.invisibility_of_element(Element))

定位方式：
xpath:在appium和selenium中都可以使用

appium 原生控件不支持 css selector 进行定位
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium():
    def setup(self):
        self.driver = webdriver.chrome()
        self.driver.get("https://inv.mxcloud.work/sign")

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
