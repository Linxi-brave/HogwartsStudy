from util.read_ini import ReadIni
from log.user_log import UserLog
import time
class FindElement(object):
    def __init__(self,driver,filename=None,node=None):
        self.driver = driver
        self.log = UserLog()
        self.logger = self.log.get_log()
        self.filename = filename
        self.node = node


    def get_element(self,key):
        read_ini = ReadIni(self.filename,self.node)
        local = read_ini.get_value(key)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            print(by)
            print(local_by)
            try:
                if by == 'id':
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)
                    self.logger.info(self.driver)
                    self.logger.info(self.driver.find_element_by_id(local_by))
                    time.sleep(2)
                    # self.driver.find_element_by_id
                    print(local)
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    self.logger.info("-------get_element----by---localby--")
                    return self.driver.find_element_by_class_name(local_by)
                elif by == "Name":
                    self.logger.info("-------get_element----by---localby--")
                    return self.driver.find_element_by_name(local_by)

                elif by == "ids":
                    self.logger.info("-------get_element----by---localby--")
                    return self.driver.find_elements_by_id(local_by)  #获取一个 WebElement的列表

                elif by == "xpath":
                    element = self.driver.find_element_by_xpath(local_by)
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)
                    self.logger.info(self.driver)
                    print(element)
                    print(local_by)
                    return element

                elif by == 'xpaths':
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)
                    self.logger.info(self.driver)
                    return self.driver.find_elements_by_xpath(local_by)

                elif by == 'name':
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)
                    self.logger.info(self.driver)
                    #iOS的定位方式，主要使用元素的label和name，如果这个属性值为空，则不能使用这个进行定位
                    return self.driver.find_element_by_accessibility_id(local_by)
                elif by == "predicate":
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)

                    #iOS的定位方式，使用原生支持的predicate定位方式，该定位方式速度较快，可支持元素的单个属性和多个属性的定位
                    #例子：单属性 ："value == 'ClearEmail'" ；多属性 ："type == 'XCUIElementTypeButton' AND value == 'ClearEmail'
                    element = self.driver.find_element_by_ios_predicate(local_by)
                    if element == None:
                        self.logger.info("element为None")
                    self.logger.info(element)
                    print(element)
                    print(local_by)
                    return element
                elif by == 'predicates':
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)
                    elements = self.driver.find_elements_by_ios_predicate(local)
                    if elements == None:
                        self.logger.info("elements 为None")
                    self.logger.info(elements)
                    return elements
                elif by == 'accessibility_id':
                    try:
                        self.logger.info("-------get_element----by---localby--")
                        self.logger.info(by)
                        self.logger.info(local_by)
                        # self.logger.info(self.driver)

                        element = self.driver.find_element_by_accessibility_id(local_by)
                        if element == None:
                            self.logger.info("element---->None")
                        self.logger.info(element)
                        print(element)
                        print(local_by)
                        return element
                    except:
                        self.logger.error(self.driver.find_element_by_xpath(local_by))
                else:
                    self.logger.info("-------get_element----by---localby--")
                    self.logger.info(by)
                    self.logger.info(local_by)
                    self.logger.info(self.driver)
                    print(local)
                    self.logger.info(self.driver.find_element_by_xpath(local_by))

                    return self.driver.find_element_by_xpath(local_by)


            except:
            # self.driver.save_screenshot("../jpg/test02.png")
                return None

        else:
            return None

