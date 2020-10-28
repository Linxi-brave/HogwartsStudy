from appium import webdriver
import os
import time
class BaseDriver(object):
    def __init__(self):
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

        # 设置手机设备信息
        # 初始化
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '10.3.10.0'  # 设备系统版本
        desired_caps['deviceName'] = 'Redmi111'  # 设备名称
        desired_caps['udid'] = '56f46ae7'  # 设备名称
        # 设置APP信息，进入启动页

        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(1)
    def get_driver(self):
        self.driver = self.driver
        return self.driver

    def click_agreen(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
if __name__ == '__main__':

    dr = BaseDriver()
    time.sleep(3)
    dr.click_agreen()

'''
'''