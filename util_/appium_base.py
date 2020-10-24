from appiumbase.find_element import FindElement
from selenium.webdriver.support.ui import WebDriverWait
import time
from util.get_time import mytime
'''
封装操作 Appium 元素的类及相关函数
包含了 iOS 和 Android 操作
包含了 关键字驱动测试中从Excel函数获取element的定位方式和值，以及直接从driver中操作元素的函数
'''
class ActionMethod(object):
    def __init__(self,driver,filename = None,node = None):
        self.driver = driver
        if filename == None:
            self.filename = '/Users/huangwenjiao/TestingScript/po-testscript/teamkitios/iOSconfig/teamkitElement.ini'
        else:
            self.filename = filename
        if node == None:
            self.node = 'loginelement'
        else:
            self.node = node
        self.mtime = mytime()
        self.get_by_local = FindElement(driver,self.filename,self.node)


    def on_click_element(self,*args):
        '''
        该函数先获取到 elements ， 之后获取 agrs[1]为点击elemnets列表中的第n个elemnet
        :param args: *args 从excel 表格中获取 ，一般格式为 ： args[0]为定位值，例子：teamicons ；args[1]为第n个参数，例子 ：0
        :return: 执行了点击 element 的操作
        '''
        element = self.get_by_local.get_element(args[0])
        n = int(args[1])
        if element == None:
            return args[0],"元素没有找到"
        try:
            element[n].click()
            return True
        except Exception as e:
            print(e)

    def input_int_str(self, *args):
        '''
        由于在excel表格中获取到的手机号为float类型，但是我需要为文本类型，所以这里把所有输入为手机号、密码等都转为文本类型输入
        :param args: *args 从excel表格中获取，args[0]为元素定位值，args[1]为输入的值，如手机号
        :return: 执行了 在input中输入 args[1]的值
        '''
        # key,value
        element = self.get_by_local.get_element(args[0])
        print(element)
        if element == None:
            return args[0], "元素没找到"

        value = int(args[1])
        value = str(value)
        element.send_keys(value)
        time.sleep(2)
        return True

    def input(self, *args):
        # key,value
        '''
        该函数执行appium中的元素输入文案
        :param args: args 从excel表格中获取，args[0]为元素定位值，args[1]为输入的值，如手机号
        :return: 执行了 在input中输入 args[1]的值
        '''
        element = self.get_by_local.get_element(args[0])
        print(element)
        if element == None:
            return args[0], "元素没找到"
        print(args[0])
        print(args[1])
        value = str(args[1]) + str(self.mtime.datetime())
        try:
            element.send_keys(value)
        except Exception as e:
            print(e)
        return True

    def clearinput(self, *args):
        # key,value
        '''
        该函数执行appium中的元素先清空输入框的内容，然后再输入文案
        :param args: args 从excel表格中获取，args[0]为元素定位值，args[1]为输入的值，如手机号
        :return: 执行了 在input中输入 args[1]的值
        '''
        element = self.get_by_local.get_element(args[0])
        print(element)
        if element == None:
            return args[0], "元素没找到"
        value = str(args[1]) + str(self.mtime.datetime())
        try:
            element.clear()
            element.send_keys(value)
        except Exception as e:
            print(e)
        return True

    def textinput(self, *args):
        # key,value
        '''
        该函数执行appium中的元素输入内容，不需加时间后缀
        :param args: args 从excel表格中获取，args[0]为元素定位值，args[1]为输入的值，如手机号
        :return: 执行了 在input中输入 args[1]的值
        '''
        element = self.get_by_local.get_element(args[0])
        print(element)
        if element == None:
            return args[0], "元素没找到"
        value = str(args[1])
        try:
            element.clear()
            element.send_keys(value)
        except Exception as e:
            print(e)
        return True

    def onclickinput(self, *args):
        # key,value
        '''
        该函数执行appium中的元素点击元素，然后输入文案
        :param args: args 从excel表格中获取，args[0]为元素定位值，args[1]为输入的值，如手机号
        :return: 执行了 在input中输入 args[1]的值
        '''
        element = self.get_by_local.get_element(args[0])
        print(element)
        if element == None:
            return args[0], "元素没找到"
        print(args[0])
        print(args[1])
        value = str(args[1]) + str(self.mtime.datetime())
        try:
            element.click()
            element.send_keys(value)
        except Exception as e:
            print(e)
        return True
    def onclickclearinput(self, *args):
        # key,value
        '''
        该函数执行appium中的元素先点击输入框，显示键盘，再点击清除输入框内容，再输入内容
        :param args: args 从excel表格中获取，args[0]为元素定位值，args[1]为输入的值，如手机号
        :return: 执行了 在input中输入 args[1]的值
        '''
        element = self.get_by_local.get_element(args[0])
        print(element)
        if element == None:
            return args[0], "元素没找到"
        value = str(args[1])
        try:
            element.click()
            element.clear()
            element.send_keys(value)
        except Exception as e:
            print(e)
        return True

    def on_click(self, *args):
        '''
        点击单个元素函数
        :param args:
        :return:
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0],"元素没找到"
        element.click()
        time.sleep(1)
        return True

    # 获取屏幕的宽高
    def get_size(self):
        '''
        获取手机屏幕的宽高
        :return: width 为宽 ， height为高
        '''
        size = self.get_by_local.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height
    #向左边滑动
    def swipe_left(self):
        '''
        向左滑动
        :return:
        '''
        #[100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.get_by_local.driver.swipe(x1, y1, x, y1, 2000)

    def swipe_right(self):
        '''
        右滑
        '''
        #[100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.get_by_local.driver.swipe(x1, y1, x, y1, 2000)
        return True

    def swipe_up(self):
        #[100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10*2
        self.get_by_local.driver.swipe(x1, y1, x1, y, 1000)
        return True

    def swipe_down(self):
        #[100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.get_by_local.driver.swipe(x1, y1, x1, y)
        return True

    def swipe_any_any(self,x1,y1,x2,y2,time = None):
        '''
        封装从点到点的滑动，从 （x1,y1) 滑动到 （x2,y2)
        :param x1: 开始点的 x 轴坐标
        :param y1: 开始点的 y 轴坐标
        :param x2: 结束点的 x 轴坐标
        :param y2: 结束点的 y 轴坐标
        :param time: 滑动的速度
        :return: 执行了滑动
        '''
        if time == None:

            self.get_by_local.driver.swipe(x1, y1, x2, y2, 1000)
        else:
            self.get_by_local.driver.swipe(x1,y1,x2,y2,time)
            return True
    #从A点到B点的滑动，输入格式例子：0.8,0.2,0.8,0.3
    def swipe_any_any_per_args(self,*args):
        '''
        封装从点到点的滑动，从 （x1,y1) 滑动到 （x2,y2) ,参数输入的是从excel表格中获取的，且获取的数据为比例型
        :param x1: 开始点的 x 轴坐标的比例
        :param y1: 开始点的 y 轴坐标的比例
        :param x2: 结束点的 x 轴坐标的比例
        :param y2: 结束点的 y 轴坐标的比例
        :param time: 滑动的速度
        :return: 执行了滑动
        '''
        point = args[0]
        pointlist = point.split(',')
        xper1 = pointlist[0]
        yper1 = pointlist[1]
        xper2 = pointlist[2]
        yper2 = pointlist[3]
        x1 = self.get_size()[0] * xper1
        y1 = self.get_size()[1] * yper1
        x2 = self.get_size()[0] * xper2
        y2 = self.get_size()[1] * yper2

        self.get_by_local.driver.swipe(x1, y1, x2, y2)
        return True
    def swipe_any_any_per(self,xper1,yper1,xper2,yper2):
        '''
        封装从点到点的滑动，从 （x1,y1) 滑动到 （x2,y2)，且获取的数据为比例型
        :param x1: 开始点的 x 轴坐标的比例
        :param y1: 开始点的 y 轴坐标的比例
        :param x2: 结束点的 x 轴坐标的比例
        :param y2: 结束点的 y 轴坐标的比例
        :param time: 滑动的速度
        :return: 执行了滑动
        '''
        x1 = self.get_size()[0] * xper1
        y1 = self.get_size()[1] * yper1
        x2 = self.get_size()[0] * xper2
        y2 = self.get_size()[1] * yper2

        self.get_by_local.driver.swipe(x1, y1, x2, y2)
        return True



    def sendkeysreturn(self,*args):
        '''
        调起输入键盘，输入内容后，需要点击回车确定发送或者收起键盘。这里是发送换行，为点击return 按钮作用
        :return:
        '''
        element = self.get_by_local.get_element(args[0])
        if element !=None:
            element.send_keys("\n")
            time.sleep(2)
        return True

    def get_element(self, *args):
        '''
        传入定位方式，返回可操作的element
        :param args: 从excel表格中获取的定位方式
        :return: element
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return None
        return element

    def press_keycode(self,*args):
        '''
        强制取消键盘，由于 appium 、xcode 版本问题，导致的首次输入中英文时提示无法点击键盘，网上说这个方法
        :param  args :传入取消键盘后的延迟时间，单位为秒
        :return:
        '''
        self.driver.press_keycode(4)
        self.driver.hide_keyboard()

        time.sleep(int(args[0]))



    def launchdriver(self):
        '''
        启动 APP ,相当于冷启动APP
        :return:执行了启动APP
        '''
        self.get_by_local.driver.launch

    def clickpoit(self,X,Y):
        '''
        对于某些无法获取到元素，但是需要点击，这个时候直接点击某一点
        :param X:点击某点的X轴坐标
        :param Y:点击某点的Y轴坐标
        :return:执行了点击某点
        '''
        self.get_by_local.driver.tap([(X, Y)])
        return True

    def clickpoitper(self,xper,yper):
        '''
        对于某些无法获取到元素，但是需要点击，这个时候直接点击某一点
        :param X:点击某点的X轴坐标的比例值
        :param Y:点击某点的Y轴坐标的比例值
        :return:执行了点击某点
        '''
        X = xper * self.get_size()[0]
        Y = yper * self.get_size()[1]
        self.clickpoit(X,Y)
        return True

    def startactivity(self,page,actvity):

        self.get_by_local.driver.start_activity(page, actvity)

    def wait_activity(self, activity, timeout, interval=1):

        try:
            WebDriverWait(self, timeout, interval).until(
                lambda d: d.current_activity == activity)
            return True
        except :
            return False

    def clickpoint(self,xper,yper):
        size = self.get_element()
        width = size[0]
        height = size[1]
        x = width * xper
        y = height * yper
        self.driver.tap([x,y],500)
        return True

    def clickpointagrs(self,*agrs):
        '''
        该函数传入 *agrs 为点的坐标比例值，例子：0.5,0.85 ，第一个为X轴坐标，第二个为Y轴坐标；执行了点击某点
        :param agrs: *agrs为excel表格中获取的数据 ，args[0]为点的数据
        :return: 执行了点击某点
        '''
        point = agrs[0].split(",")
        xper = point[0]
        yper = point[1]
        size = self.get_size()
        width = size[0]
        height = size[1]
        x = int(width) * float(xper)
        y = int(height) * float(yper)
        self.driver.tap([(x,y)],500)
        return True

    #iOS 平台
    #获取按钮是否可点击的状态
    def isenabled(self):
        '''
        iOS 平台有isenabled ，可用于断言
        :return: 元素可点击则返回 True ，元素不可点击则返回 False
        '''
        enabled = self.driver.find_element_by_name("enabled")
        if enabled == "true":
            return True
        elif enabled == "false":
            return False

    #iOS平台
    #获取元素是够可见状态
    def isvisible(self):
        isvisible = self.driver.find_element_by_name("visible")
        if isvisible == 'true':
            return True
        else:
            return False


    def sleep_time(self, *args):
        '''
        该函数为停留不进行操作，*args[0] 传入单位为秒，如 1 代表停留1秒
        :param args:
        :return: 执行了停留时间
        '''
        try:
            time.sleep(int(args[0]))
            return True
        except Exception as e:
            print(e)
            return False

    # 获取屏幕的宽高
    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)
        return True

    # 向右边滑动
    def swipe_right(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)
        return True

    # 向上滑动
    def swipe_up(self, *args):
        #[100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10*2
        self.driver.swipe(x1, y1, x1, y, 1000)
        return True

    # 向下滑动
    def swipe_down(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)
        return True

    def get_element(self, *args):
        print(args)
        print(args[0])
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return None
        return element
    #ios 处理系统弹框，默认都接受
    def iosalertaccept(self):
        '''
        appium中出现系统弹框，不好处理，这个函数为默认都点击接受
        :return:
        '''
        self.driver.switch_to.alert.accept()
    #向上滑动元素
    # left、right、up、down方便对应左、右、上、下
        return True

    def swipeelementup(self, *args):

        element = self.get_by_local.get_element(args[0])
        self.driver.execute_script("mobile:swipe", {"direction": "up", 'element': element, "duration": 0.02})

    def swipeelementdown(self, *args):

        element = self.get_by_local.get_element(args[0])
        self.driver.execute_script("mobile:swipe", {"direction": "down", 'element': element, "duration": 1})

    def swipeelementright(self, *args):

        element = self.get_by_local.get_element(args[0])
        self.driver.execute_script("mobile:swipe", {"direction": "right", 'element': element, "duration": 1})

    def swipeelementleft(self, *args):

        element = self.get_by_local.get_element(args[0])
        self.driver.execute_script("mobile:swipe", {"direction": "left", 'element': element, "duration": 1})
    def swipeelementpoints(self, *args):

        '''
        操作appium元素，从当前屏幕上的一点滑动到另外一点
        :param args: args[1]为点的坐标比例
        :return:
        '''
        try:
            element = self.get_by_local.get_element(args[0])
        except:
            element = None

        point = args[1]
        pointlist = point.split(',')
        xper1 = pointlist[0]
        yper1 = pointlist[1]
        xper2 = pointlist[2]
        yper2 = pointlist[3]

        x1 = self.get_size()[0] * xper1
        y1 = self.get_size()[1] * yper1
        x2 = self.get_size()[0] * xper2
        y2 = self.get_size()[1] * yper2
        self.driver.execute_script("mobile:dragFromToForDuration",{"duration": 0.5, "element": element, "fromX": x1, "fromY": x2, "toX": y1, "toY": y2})

    def launch_app(self,*args):
        '''
        启动APP，前台切后台，冷启动；启动后停留n秒，args[0]为停留的时间
        :param args:agrs[0]
        :return:
        '''
        # self.get_by_local.get_element(args[0])
        self.driver.launch_app()
        time.sleep(args[0])


   # 断言title
    # 成功返回为 true
    def assertistitle(self, *args):
        '''
        断言函数，传入的args为参数，若 元素值 有值，则 args[0] 为元素值的定位方式，若 元素值没有值，则args[0]为 预期操作值
        断言为title ，元素为界面的title，不需特殊获取元素，只需断言标题是否与同一致
        该函数不适合原生APP操作，适合H5
        :param args:
        :return:
        '''
        titletext = args[0]
        if titletext in self.driver.title:
            return True
        else:
            return False

    # 断言内容
    def assertpagesource(self, *args):
        '''
        断言函数，args 为参数，传入为从excel中获取的预期操作值；判断界面是否有内容，有则返回True
        :param args:
        :return:
        '''
        text = args[0]

        if text in self.driver.page_source :
            return True
        else:
            return False

    def assertpagesourceaddtime(self,*args):
        '''
        断言函数，校验页面中有预期结果，输入文案例子：标题>time ，实际界面显示的文案为 ：标题2020-02-02
        :return: 校验为真返回为 True
        '''
        textadd = args[0]
        if '>' in textadd:
            textfor = textadd.split(">")[0]
            timetext = str(self.mtime.datetime())
            text = textfor + timetext
            if text in self.driver.page_source:
                return True
            else:
                return False
    # 断言内容
    def assertnopagesource(self, *args):
        '''
        断言函数，判断界面不应存在内容
        :param args:
        :return:
        '''
        text = args[0]
        if text not in self.driver.page_source:
            return True
        else:
            return False

    # 元素属性断言
    def assertgetattribite(self, *args):
        '''
        断言函数，界面存在某个元素，这个元素的text值为对应的值，对应则返回为True,不对应则返回为False
        :param args:  args[0]为元素值；args[1]为对应断言的值
        :return: 断言成功则返回为 True
        '''

        element = self.get_by_local.get_element(args[0])
        try:
            expectvalue = args[1]

            if element == None:
                print("element -->None")
                # break
            else:
                value = element.get_attribute("value")
                print("value----------------------->")
                print(value)
                if value == expectvalue:
                    print("true")
                    return True
                elif value != expectvalue:
                    return False

        except Exception as e:
            print(e)
    def assertisenable(self,*args):
        element = self.get_by_local.get_element(args[0])
        try:
            isenabele = element.is_enabled()
            if isenabele==True:
                return True
            else:
                return False
        except Exception as e:
            print(e)




    def asserttextinelements(self,*args):
        '''
        断言函数，传入参数 args[1] 为"today",则校验元素value值存在为今天日期；若args[1]为其他，则校验元素的value值同传入的文案
        :param args: args[1]为断言值
        :return: 成功返回为True
        '''
        elements = self.get_by_local.get_element(args[0])
        text = args[1]
        if str(text) == "today":
            text = str(self.mtime.datetime())
        for i in len(elements):
            value = elements[i].get_attribute("value")
            if text in value :
                return True
            else:
                return False
    def assertequal(self,*args):
        '''
        断言函数，两个值相等则返回为true
        :param args:
        :return:
        '''
        text1 = args[0]
        text2 = args[1]
        try:
            self.assertequal(text1,text2)
            return True
            self.logger.info("断言assertequal : text1:"+ text1 + "text2" + text2)
        except:
            self.savescreen()
            self.logger.info(self.baseaction.logerror())
            return False

    def assertnotequal(self,text1,text2):
        try:
            self.assertnotequal(text1 ,text2)
            self.logger.info("断言assertequal : text1:"+ text1 + "text2" + text2)
        except:
            self.savescreen()
            self.logger.info(self.baseaction.logerror())
