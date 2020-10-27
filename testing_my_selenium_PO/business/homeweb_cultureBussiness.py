from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.pagehandle.homeweb_culturePage import HomewebCulturePage


class HomewebCultureBussiness():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.action = SeleniumAction(self.driver)

        self.culturePage = HomewebCulturePage(self.driver)

    def goto_createpage(self):

        self.culturePage.goto_createpage()

    def create_culture(self,titleinput,contextinput):

        if titleinput != None:
            self.action.sendkeys_ele(
                self.culturePage.getelement_cultitleinput(),titleinput
            )

        if contextinput!= None:
            self.action.sendkeys_ele(
                self.culturePage.getelement_culcontextinput(),contextinput
            )

        self.action.swipeup()

        self.action.click_ele(self.culturePage.getelment_createbtn())


    def create_linkculture(self,linkinput):

        eles = self.driver.find_elements_by_xpath("//div[@id='publishFind']//nav//button")

        eles[1].click()

        # self.action.click_ele(self.culturePage.getelement_linkbtn())

        if linkinput != '':
            self.action.sendkeys_ele(
                self.culturePage.getelement_culhrefinput(),linkinput
            )

        try :
            self.action.click_ele(self.culturePage.getelement_culbtn())

        except:

            return False

        self.action.click_ele(self.culturePage.getelment_createbtn())




