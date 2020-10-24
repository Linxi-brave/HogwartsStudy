import sys
from log.user_log import UserLog
class BaseAction(object):
    def __init__(self,driver=None):
        self.log = UserLog()
        self.logger = self.log.get_log()
        self.iferror = True
        self.driver = driver

    def logerror(self):
        exec_type, exec_obj, exec_tb = sys.exc_info()
        #没有出现异常
        if exec_obj == None:
            self.iferror = True
        #出现异常
        else:
            fname = exec_tb.tb_frame.f_code.co_filename
            self.iferror = False
            return exec_type, exec_obj, exec_tb

    #打印错误信息到日志
    def errorloginfo(self):
        iferror = self.logerror()
        if iferror == False:
            self.logger.error(self.logerror())


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

