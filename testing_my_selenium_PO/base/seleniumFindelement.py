from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from util.read_ini import ReadIni
from util.user_log import UserLog
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
class FindElement:

    def __init__(self,driver,filename=None,node=None):
        self.driver = driver
        self.log = UserLog()
        self.logger = self.log.get_log()
        self.filename = parent_dir +'/config/Element.ini'
        self.rean_ini= ReadIni(filename=self.filename,node=node)
        self.logger.info(filename)
        self.logger.info(node)

    def get_element(self,key):
        '''
        获取元素，返回Selenium Element元素
        '''

        data = self.rean_ini.get_value(key)
        self.logger.info(key)
        self.logger.info(data)
        by = data.split('>')[0]
        value = data.split('>')[1]

        self.logger.info('定位方式' + by + '定位值' + value)
        try:
            if by == 'id':
                ele = self.driver.find_element_by_id(value)
                return ele

            elif by == 'xpath':

                ele = self.driver.find_element_by_xpath(value)
                return ele
            elif by == 'css':

                ele = self.driver.find_element_by_css_selector(value)
                return ele

            elif by == 'link_text':
                ele = self.driver.find_element_by_link_text(value)
                return ele

            elif by == 'name':
                ele = self.driver.find_element_by_name(value)
                return ele

            elif by == 'classname':
                ele =  self.driver.find_element_by_class_name(value)
                return ele

            elif by == 'xpaths':
                ele = self.driver.find_elements_by_xpath(value)
                return ele

            elif by == 'classnames':
                ele = self.driver.find_elements_by_class_name(value)
                return ele
            elif by == 'linktexts':
                ele = self.driver.find_elements_by_link_text(value)
                return ele
        except :
            self.logger.info(self.log.iferrorinfo())

    def get_childelement(self,elements,key):
        '''
        获取元素
            '''
        data = self.rean_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                ele = elements.find_element_by_id(value)
                return ele
            elif by == 'xpath':
                ele = elements.find_element_by_xpath(value)
                return ele
        except:
            self.logger.info(self.log.iferrorinfo())


