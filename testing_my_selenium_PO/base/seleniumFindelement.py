from time import sleep

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from util.read_ini import ReadIni
from util.user_log import UserLog
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
from selenium.webdriver.support import expected_conditions as EC

class FindElement:

    def __init__(self,driver:WebDriver,file=None,node=None):
        self.driver = driver
        self.log = UserLog()
        self.logger = self.log.get_log()
        if file == None:
            self.filename = parent_dir +'/config/Element.ini'
        else:
            self.filename = parent_dir + file
        self.rean_ini= ReadIni(filename=self.filename,node=node)
        self.logger.info(self.filename)
        self.logger.info(node)

    def get_element(self,key):
        '''
        获取元素，返回Selenium Element元素
        '''

        data = self.rean_ini.get_value(key)
        self.logger.info(key)
        self.logger.info(data)
        by = data.split('>')[0]
        values = data.split('>')[1:]

        if len(values) == 1:

            value = data.split('>')[1]

        elif len(values) > 1:

            value = values[0]

            for i in range(1,len(values) - 1):

                value = value + '>' + values[i]


        self.logger.info('定位方式' + by + '定位值' + value)
        # self.logger.info(type(value))
        try:
            if by == 'id':

                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(value))
                is_disappeared = WebDriverWait(self.driver , 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id(value).is_displayed())

                # locator = (By.ID,"value")
                # WebDriverWait(self.driver,20,0.5).until(EC.presence_of_all_elements_located(locator))
                # ele = self.driver.find_element_by_id(value)
                return element

            elif by == 'xpath':

                ele = WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath(value))
                # ele = self.driver.find_element_by_xpath(value)
                self.logger.info("获取到的元素为--->")
                self.logger.info(ele)
                return ele

            elif by == 'css':
                # locator = (By.CSS_SELECTOR,"value")
                # WebDriverWait(self.driver,20,0.5).until(EC.presence_of_all_elements_located(locator))
                ele = self.driver.find_element_by_css_selector(value)
                self.logger.info("获取到的元素为--->")
                self.logger.info(ele)
                return ele

            elif by == 'link_text':
                WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element(
                    self.driver.find_element_by_link_text(value)
                ))
                ele = self.driver.find_element_by_link_text(value)
                return ele

            elif by == 'name':
                WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element(
                    self.driver.find_element_by_name(value)
                ))
                ele = self.driver.find_element_by_name(value)
                return ele

            elif by == 'classname':

                locator = (By.CLASS_NAME,value)
                WebDriverWait(self.driver,20,0.5).until(EC.presence_of_all_elements_located(locator))
                ele =  self.driver.find_element_by_class_name(value)
                return ele

            elif by == 'xpaths':
                # locator = (By.XPATH,value)
                # WebDriverWait(self.driver,10,0.5).until(
                #     expected_conditions.presence_of_all_elements_located(locator)
                # )
                # ele = self.driver.find_elements(locator)
                sleep(4)
                ele = self.driver.find_elements_by_xpath(value)
                self.logger.info("获取到的元素为--->")
                self.logger.info(ele)
                return ele

            elif by == 'classnames':
                locator = (By.CLASS_NAME,value)
                WebDriverWait(self.driver,20,0.5).until(EC.presence_of_all_elements_located(locator))

                eles = self.driver.find_elements_by_class_name(value)
                self.logger.info("获取到的元素为--->")
                self.logger.info(eles)
                return eles
            elif by == 'linktexts':
                WebDriverWait(self.driver,20,0.5).until(expected_conditions.invisibility_of_element(
                    self.driver.find_elements_by_link_text(value)
                ))
                ele = self.driver.find_elements_by_link_text(value)
                return ele

        except :
            print("11112222")
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


