import time

from selenium.webdriver import ActionChains, TouchActions



class SeleniumAction:
    def __init__(self,driver):
        self.driver = driver

    def click_ele(self,ele):
        ele.click()

    def sendkeys_ele(self,ele,value):
        ele.send_keys(value)

    def actoinchain_click(self,ele):
        '''
        使用 ActionChain 对元素进行单击，传入参数 ele 为元素
        :param ele: 元素
        '''
        action = ActionChains(self.driver)
        action.click(ele)
        action.perform()

    def actionchain_contextclick(self,ele):
        '''
        使用 ActionChain 对元素进行右击，传入参数 ele为元素
        :param ele: 元素
        '''
        action = ActionChains(self.driver)
        action.context_click(ele)
        action.perform()

    def actionchain_doubleclick(self,ele):
        '''
        使用 ActionChain对元素进行双击，传入参数 ele为元素
        :param ele: 元素
        '''
        action = ActionChains(self.driver)
        action.double_click(ele)
        action.perform()

    def actionchain_movetoelement(self,ele):
        '''
        使用 ActionChain 将光标移动到元素上
        :param ele: 元素
        '''
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    def actionchain_dragdrop(self,ele1,ele2):
        '''
        使用 ActionChain 将元素1拖动到元素2上面
        :param ele1: 元素1
        :param ele2: 元素2
        '''
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2)
        action.perform()

    def actionchain_keys(self,ele,key,second):
        '''
        使用 ActionChain 模拟键盘操作
        :param ele: 元素输入框
        :param key: 键盘数字
                    Keys.BACKSPACE = '\ue003'
                    Keys.BACK_SPACE = BACKSPACE
        '''
        ele.click()
        action = ActionChains(self.driver)
        # action.send_keys(Keys.BACK_SPACE)
        action.send_keys(key).pause(second) # pause(1) 延时1秒，观看效果
        action.perform()

    def touchaction_scrollbottom(self,ele):
        '''
        使用 TouchActions 实现界面滑动到底部
        :param ele:
        '''
        action = TouchActions(self.driver)
        action.scroll_from_element(ele,0,10000)
        action.perform()

    def switch_windows(self,n):
        '''
        切换当前操作的窗口
        :param 第n个窗口
        '''
        print(self.driver.current_window_handle) # 打印当前窗口
        print(self.driver.window_handles) # 打印所有窗口
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[n])

    def switch_frame(self,frameId):
        '''
        切换frame进行操作
        '''
        self.driver.switch_to_frame(frameId)

    def alert_accept(self):
        '''
        点击alert弹框中的同意按钮
        '''
        self.driver.switch_to_alert().accept()
    def alert_dismiss(self):
        '''
        点击alert弹框中的拒绝按钮
        '''
        self.driver.switch_to_alert.dismiss()

    def execute_jsscript(self,jsscript):
        '''
        执行js语句
        '''
        self.driver.execute_script(jsscript)

    def get_title(self):
        '''
        获取界面title
        '''
        title = self.driver.title
        return  title

    def get_elementtext(self,ele):
        '''
        返回元素的值
        '''
        elementtext = ele.text
        return elementtext

    def get_elementattribute(self,ele,attribute):
        '''
        获取元素的属性值
        :param ele: 元素
        :param attribute: 属性值
        '''
        # elementattribute = ele.get_attribute("textContent")
        elementattribute = ele.get_attribute(attribute)
        return elementattribute

    def inputfile(self,inputele,filepath):
        '''
        文件上传
        '''
        inputele.send_keys(filepath)

        #向左滑动
    def swipeleft(self):
        x1 = self.getsize()[0] /10
        x2 = self.getsize()[0] /10 * 9
        y1 = self.getsize()[1] /2

        self.driver.swipe(x1,y1,x2,y1,2000)

    # 向右滑动
    def swiperight(self):
        x1 = self.getsize()[0] / 10
        x2 = self.getsize()[0] / 10 * 9
        y1 = self.getsize()[1] / 2
        self.driver.swipe(x2, y1, x1, y1, 2000)

    # 向上滑动
    def swipeup(self):
        y1 = self.getsize()[1] / 10
        y2 = self.getsize()[1] / 10 * 9
        x1 = self.getsize()[0] / 2
        self.driver.swipe(x1, y1, x1, y2, 2000)

    # 向下滑动
    def swipedown(self):
        y1 = self.getsize()[1] / 10
        y2 = self.getsize()[1] / 10 * 9
        x1 = self.getsize()[0] / 2
        self.driver.swipe(x1, y2, x1, y1, 2000)

    #浏览器返回上一界面
    def driverback(self):

        self.driver.back()
        time.sleep(2)

