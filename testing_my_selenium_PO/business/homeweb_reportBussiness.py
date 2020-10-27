from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.pagehandle.homeweb_reportPage import HomewebReportPage


class HomewebReportBussiness():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.reportpage = HomewebReportPage(self.driver)

        self.action = SeleniumAction(self.driver)

    def createSaleReport(self,sale,content):


        self.action.sendkeys_ele(self.reportpage.getelement_saleinput(),sale)

        self.action.sendkeys_ele(
            self.reportpage.getelement_input(),content
        )

    def creatReport(self,summary,plan,type='day',sale=None,content=None):

        eles = self.reportpage.getelemts_reporttypes()

        if type == 'day':

            self.action.click_ele(eles[0])

        elif type == 'week':

            self.action.click_ele(eles[1])

        elif type == 'month':

            self.action.click_ele(eles[2])

        else :


            self.action.click_ele(eles[3])

            self.createSaleReport(sale,content)

        if summary != None:

            self.action.sendkeys_ele(self.reportpage.getelement_jobsuminput()
                                 ,summary)
        if plan != None:
            self.action.sendkeys_ele(self.reportpage.getelement_jobplaninput()
                                 ,plan)

        self.action.click_ele(self.reportpage.getelement_createbtn())



