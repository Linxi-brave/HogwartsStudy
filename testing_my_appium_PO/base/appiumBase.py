import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

from util.read_ini import ReadIni
from util.user_log import UserLog
parent_dir = os.path.abspath(os.path.join(os.getcwd(),'../..'))

class AppiumBase:

    def __init__(self,platformName=None,platformVersion=None,deviceName=None,udid=None,appPackage=None,appActivity=None):

        if platformName == None:

            platform = 'Android'

        else:

            platform = platformName

        if platformVersion == None:

            version = '10.3.10.0'

        else:
            version = platformVersion

        if deviceName == None:

            device = 'Redmi111'

        else:
            device = deviceName

        if udid == None:

            udi = '56f46ae7'

        else :

            udi = udid

        if appPackage == None:
            Package = 'com.xueqiu.android'
        else:
            Package = appPackage

        if appActivity == None:

            Activity =   'com.xueqiu.android.view.WelcomeActivityAlias'
        else :
            Activity = appActivity


        desired_caps = {}
        desired_caps['platformName'] = platform  # 设备系统
        desired_caps['platformVersion'] = version  # 设备系统版本
        desired_caps['deviceName'] = device  # 设备名称
        desired_caps['udid'] = udi  # 设备名称

        # 设置APP信息，进入启动页

        desired_caps['appPackage'] = Package
        desired_caps['appActivity'] = Activity
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        self.driver.implicitly_wait(3)  # 初始化 webdriver 之后，因式等待3秒

        self.log = UserLog()
        self.logger = self.log.get_log()

        # 初始化读取元素定位信息类
        filename = parent_dir + '/config/AppElement.ini'

        node = 'AppElement'

        self.read_ini = ReadIni(filename=filename,node= node)




    def get_element(self,key):

        # read_ini = ReadIni(filename,node)
        '''封装查找元素'''

        local = self.read_ini.get_value(key)
        try:

            if local != None:
                by = local.split('>')[0]
                local_by = local.split('>')[1]

                if by == 'id':

                    return self.driver.find_element_by_id(local_by)

                elif by == 'classname':

                    return self.driver.find_element_by_class_name(local_by)

                elif by == 'name':

                    return self.driver.find_element_by_name(local_by)

                elif by == 'xpath':

                    return self.driver.find_element_by_xpath(local_by)

                elif by == 'ids':

                    return self.driver.find_elements_by_id(local_by)

                elif by == 'accessibility_id':

                    return self.driver.find_element_by_accessibility_id(local_by)


                elif by == 'xpaths':

                    return self.driver.find_elements_by_xpath(local_by)

                elif by == 'mobile_id':

                    return self.driver.find_element(MobileBy.ID,local_by)

                elif by == 'mobile_ids':

                    return self.driver.find_elements(MobileBy.ID,local_by)

                elif by == 'mobile_xpath':

                    return self.driver.find_element(MobileBy.XPATH,local_by)

                elif by == 'android_uiautomator':

                    # local_by = 'new UiSelector().resourceId("com.xueqiu.android:id/login_account")'
                    # local_by = 'new UiSelector().textContains("账号密码")'
                    # local_by = 'new UiSelector().text("我的")'

                    return self.driver.find_element_by_android_uiautomator(local_by)

                elif by == 'android_uiautomators':

                    return self.driver.find_elements_by_android_uiautomator(local_by)

                else :
                    self.logger.info('没有该定位方式')


        except Exception as e:
            self.logger.info('查找元素出现异常，异常信息为：' + {e})


    def get_clildelement(self,eles:WebDriver,key):

        '''封装从父元素获取子元素'''

        data = self.read_ini.get_value(key)

        by = data.split('>')[0]

        value = data.split('>')[1]

        try:

            if by == 'id':

                ele = eles.find_element_by_id(value)

                return ele

            elif by == 'xpath':

                ele = eles.find_element_by_xpath(value)

                return ele

        except Exception as e:

            self.logger.info('查找元素出现异常，异常信息为：' + {e})


    def get_windown_rect(self):

        windown_rect = self.driver.get_window_rect()

        width = windown_rect['windth']
        height = windown_rect['height']

        return {'width':width,'height':height}



    def action_press_moveto(self):

        '''列表：屏幕操作，按住某位置后，手指移动到另外一个位置，释放手指'''

        action = TouchAction(self.driver)

        x1 = int(self.get_windown_rect()['width']/2)

        y_start = int(self.get_windown_rect()['height'] * 1/5)

        y_end = int(self.get_windown_rect()['height'] * 4/5)

        action.press(x = x1,y = y_start).wait(200).move_to(x = x1,y = y_end).release().perform()


    def action_list_find(self):

        '''列表：滑动列表数据并找到某个元素'''

        self.driver.find_elements_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0).scrollIntoView(new Uiselector().text("查找的文案")))'
        )



