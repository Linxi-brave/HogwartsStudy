#封装获取元素的element,从配置文件读取信息
#coding=utf-8
from util.read_ini import ReadIni
from log.user_log import UserLog
from  util.base import BaseAction
from util.selenium_base import SeleniumBase
import time
class FindElementele(object):
    def __init__(self,driver):
        self.driver =driver
        log = UserLog()
        self.logger = log.get_log()
        self.base = BaseAction()
        self.seleniumbase = SeleniumBase()


    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        self.logger.info("get_element: " + "定位方式"+ by + "定位值" + value)
        try:
            if by == 'id':
                while 1:
                    try:
                        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, value)))
                        self.logger.info("定位到元素：" + element)
                        time.sleep(2)
                        return element
                        break

                    except Exception as e:
                        self.base.logerror()
                        self.logger.info("还未定位到元素!")
                        self.logger.info(self.base.logerror())
                        self.seleniumbase.getlog()
                        self.seleniumbase.savescreen()


            elif by == 'name':
                while 1:
                    try:
                        return self.driver.find_element_by_name(value)

                        break
                    except:
                        self.logger.info("还未定位到元素!")
                        self.logger.info(self.base.logerror())

            elif by == 'className':
                while 1:
                    try:
                        WebDriverWait(driver, 100).until(
                            lambda driver: self.driver.find_element_by_class_name(value))

                        self.logger.info("定位到元素!")
                        time.sleep(4)
                        return self.driver.find_element_by_class_name(value)
                        break
                    except:
                        self.logger.info("还未定位到元素!")
                        self.logger.info(self.base.logerror())

            elif by == "classNames":
                while 1:
                    try:
                        return self.driver.find_elements_by_class_name(value)
                        break
                    except:
                        self.logger.info(self.base.logerror())
                        self.seleniumbase.savescreen()

            elif by == 'xpath':
                try:
                    element = self.driver.find_element_by_xpath(value)
                    self.logger.info("定位到元素" + element)
                    return element
                except Exception as e:
                    self.logger.info("还未定位到元素!")
                    self.logger.info(self.base.logerror())
                    self.seleniumbase.savescreen()

            elif by == 'xpaths':
                while 1:
                    try:
                        return self.driver.find_elements_by_xpath(value)
                        self.logger.info("定位到元素!")
                        time.sleep(2)
                        break
                    except Exception as e:
                        self.logger.info("定位方式:" + by + "--->定位值:" + value + "还未定位到元素!")
                        self.seleniumbase.savescreen()
                        time.sleep(2)
                        break
            elif by == 'link':
                while 1:
                    try:
                        return self.driver.find_element_by_link_text(value)
                        self.logger.info("定位到元素!" + element)
                        time.sleep(2)
                        break
                    except Exception as e:
                        self.logger.info("还未定位到元素!")
                        self.logger.info(self.base.logerror())
                        self.seleniumbase.savescreen()
                        break

            else:
                self.logger.info("定位方式:" + by + "--->定位值:" + value + "未知定位方式")
        except:
            print(by)
            return None

class FindElement(object):
    def __init__(self,driver,filename=None,node=None):
        self.driver =driver
        self.filename =filename
        self.node = node
        log = UserLog()
        self.logger = log.get_log()

    def get_child_nodes(self,elements,value):
        '''
        获取子节点元素的方法，返回的是子节点元素，传入父节点元素
        :return:
        '''

        if value == "id":
            try:
                element = elements.find_element_by_id(value)
                return element
            except Exception as e:
                self.logger.info("子节点元素定位失败")
                self.logger.info(e)
        elif value == 'className':
            try:
                element = elements.find_element_by_className(value)
                return element
            except Exception as e:
                self.logger.info("子节点元素定位失败")
                self.logger.info(e)



    def get_element(self,key):
        '''

        获取父节点元素的方法，传入的是父节点元素定位值
        :param key:
        :return: 返回元素
        '''
        read_ini = ReadIni(self.filename,self.node)
        print(self.filename)
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        self.logger.info("定位方式"+ by + "定位值" + key + "定位路径" + value)
        try:
            if by == 'id':
                element =  self.driver.find_element_by_id(value)
                time.sleep(2)
                return element

            elif by == 'name':

                element =  self.driver.find_element_by_name(value)

                self.logger.info(element)
                return element
            elif by == 'className':

                element =self.driver.find_element_by_class_name(value)
                self.driver.implicitly_wait(30)
                self.logger.info(element)
                return element


            elif by == 'classNames':

                time.sleep(4)
                element = self.driver.find_elements_by_class_name(value)
                self.driver.implicitly_wait(30)
                self.logger.info(element)
                return element
            elif by == 'xpath':

                element = self.driver.find_element_by_xpath(value)
                self.driver.implicitly_wait(30)
                self.logger.info(element)
                return element

            elif by == 'xpaths':

                element = self.driver.find_elements_by_xpath(value)
                self.logger.info(element)
                return element
            elif by == 'link':

                return self.driver.find_element_by_link_text(value)


            else:
                self.logger.info("定位方式:" + by + "--->定位值:" + value + "未知定位方式")

        except:
            print(by)
            self.logger.info("定位方式:" + by + "--->定位值:" + value + "还未定位到元素!")
            self.logger.info("还未定位到元素!")
            time.sleep(2)
            self.logger.info("定位方式:" + by + "--->定位值:" + value + "没有定位到元素，元素返回为 None" )
            return None


