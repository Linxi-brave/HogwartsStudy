from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumFindelement import FindElement


class HomewebCulturePage():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.findelement = FindElement(self.driver)

    def goto_createpage(self):

        self.findelement.get_element('createpage').click()

    def getelement_cultitleinput(self):

        return  self.findelement.get_element('cultitleinput')

    def getelement_culcontextinput(self):

        return self.findelement.get_element('culcontextinput')

    def getelment_createbtn(self):

        return self.findelement.get_element('culcreatebtn')

    def getelement_linkbtn(self):

        return self.findelement.get_element('linkbtn')

    def getelement_culhrefinput(self):

        return self.findelement.get_element('culhrefinput')

    def getelement_culbtn(self):

        return self.findelement.get_element('culbtn')

