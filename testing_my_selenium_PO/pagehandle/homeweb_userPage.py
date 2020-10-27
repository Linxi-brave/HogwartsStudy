from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumFindelement import FindElement


class HomewebUserPage():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.findelement = FindElement(self.driver)

    def goto_edituserpage(self):

        self.findelement.get_element('edituserpage').click()

    def getelement_inputname(self):

        return self.findelement.get_element('inputname')

    def getelement_inputEnglishname(self):

        return self.findelement.get_element('inputEnglishname')

    def getelement_inputwxname(self):

        return self.findelement.get_element('inputwxname')

    def getelement_inputfacebookname(self):

        return self.findelement.get_element('inputfacebookname')

    def getelement_usereditbtn(self):

        return self.findelement.get_element('usereditbtn')