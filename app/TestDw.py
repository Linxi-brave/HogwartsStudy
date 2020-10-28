import time

import pytest
import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.mobile import Mobile


class TestDW():

    def  setup(self):
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


    def teardown(self):
        self.driver.quit()

    def test_search(self):

        ele = self.driver.find_element_by_id('com.xueqiu.android:id/home_search')
        if ele.is_enabled() == True: # 判断是否可用
            print(ele.text)
            print(ele.location)
            print(ele.size)
            ele.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')

            ele = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and text = '阿里巴巴']")

            print(ele.is_displayed())  # 是否可见
            # ele.get_attribute('displayed')

            if ele.is_displayed() == True:
                print("搜索成功")

    def test_touchaction(self):

        action = TouchAction(self.driver)

        windorn_rect = self.driver.get_window_rect()
        width = windorn_rect["width"]
        height = windorn_rect['height']

        x1 = int(width/2)

        y_start = int(height * 1/5)
        y_end = int(height * 4/5)
        # action.release() 抬起手指
        # action.perform() 执行代码
        action.press(x=x1,y= y_start).wait(200).move_to(x=x1 ,y= y_end ).release().perform()  # 从点A按压


    def test_dingwei(self):

        # 定位方式
        self.driver.find_element_by_id('定位ID值')
        self.driver.find_element_by_id(MobileBy.ID,'定位ID值')
        self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().text("我的")'
        )
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains("账号密码")'
        )

        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")'
        )


    def test_uiautomator(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        self.driver.find_element_by_android_uiautomator('new Uiselector().resourceId("com.xueqiu.android:id/login_account")')
        self.driver.find_element_by_android_uiautomator('new Uiselector().resourceId("com.xueqiu.android:id/login_account")')

    def test_scrool_find(self):
        # 列表并找到某个元素
        self.driver.find_elements_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0).scrollIntoView(new Uiselector().text("查找的文案")))'
        )

if __name__ == '__main__':
    pytest.main()
