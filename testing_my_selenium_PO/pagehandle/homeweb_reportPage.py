from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.base.seleniumFindelement import FindElement


class HomewebReportPage():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.findelement = FindElement(self.driver)
        self.action = SeleniumAction(self.driver)

    def getelement_createbtn(self):

        return self.findelement.get_element('artcreatebtn')

    def goto_createpage(self):

        self.getelement_createbtn().click()


    def getelemts_reporttypes(self):

        eles = self.findelement.get_elements('reporttype')

        return eles

    def getelement_reporttypebtn(self):

        return self.findelement.get_element('reporttypebtn')

    def getelement_jobsuminput(self):

        return self.findelement.get_element('jobsuminput')

    def getelement_jobplaninput(self):

        return self.findelement.get_element('jobplaninput')

    def getelement_createjobbtn(self):

        return self.findelement.get_element('createjobbtn')


    def getelement_productinput(self):

        return self.findelement.get_element('productinput')

    def getelement_saleinput(self):

        return self.findelement.get_element('saleinput')

    def getelement_input(self):

        return self.findelement.get_element('input')