import urllib
import time
import os
import datetime
from log.user_log import UserLog

class SeleniumBase(object):
    # 保存图片到指定路径
    # 指定目录为当前目录下/img目录
    def __init__(self,driver):
        self.driver = driver
        self.log = UserLog()
        self.logger =self.log.get_log()
        
    #保存登录二维码
    def img(self):
        img_url = self.driver.find_element_by_xpath("//div[@class='qr-inner']/img")
        if img_url != None:
            # 保存图片数据
            data = urllib.request.urlopen(img_url).read()
            filename = int(time.time())
            filepath = os.path.join(os.getpwd()+"/img"+ filename + '.png')
            f = open('./van/' + filepath, 'wb')
            f.write(data)
            f.close()
    #截图功能
    def savescreen(self,casename):
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(os.getcwd() + '/screen/' + time +'/' + casename +'./png')
        self.driver.save_screen(filepath)

    def timeN(n):
        time = datetime.datetime.now() + datetime.timedelta(days=int(n))
        timeN = time.strftime("%Y-%m-%d %H:%M:%S")
        return timeN

    # 断言title
    # 成功返回为 true
    def assertistitle(self, titletext):
        if titletext in self.driver.title:
            return True
        else:
            return False

    # 断言内容
    def assertpagesource(self, text):
        return text in self.driver.page_source

    # 断言内容
    def assertnopagesource(self, text):
        return text not in self.driver.page_source

    # 获取元素
    def getattribite(self, element):
        return element.get_attribute()

    #浏览器返回上一界面
    def driverback(self):
        self.driver.back()

    #封装断言
    def asserttitle(self,title):
        element = self.driver.find_element_by_xpath('/html/head/title')
          #页面title
        titletext = element.text
        try :
            if self.assertEqual(titletext,title):
                self.logger.info("title 为" + title)
            else:
                self.logger.info("当前title为" + titletext)
        except:
            self.savescreen()
            self.logger.info(self.baseaction.logerror())

    def assertequal(self,text1,text2):
        try:
            self.assertequal(text1 ,text2)
            self.logger.info("断言assertequal : text1:"+ text1 + "text2" + text2)
        except:
            self.savescreen()
            self.logger.info(self.baseaction.logerror())
    def assertnotequal(self,text1,text2):
        try:
            self.assertnotequal(text1 ,text2)
            self.logger.info("断言assertequal : text1:"+ text1 + "text2" + text2)
        except:
            self.savescreen()
            self.logger.info(self.baseaction.logerror())

    # 获取selenium相关日志
    def getlog(self):
        browserlog = self.driver.get_log("browser")
        driverlog = self.driver.get_log("driver")
        clientlog = self.driver.get_log("client")
        serverlog = self.driver.get_log("server")
        self.logger.info("browserlog:" + browserlog)
        self.logger.info("driverlog" + driverlog)
        self.logger.info("clientlog" + clientlog)
        self.logger.info("serverlog" + serverlog)



    #获取屏幕的宽高
    def getsize(self):
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        return width,height


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



