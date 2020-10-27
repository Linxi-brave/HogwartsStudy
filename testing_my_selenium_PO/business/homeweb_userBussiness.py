from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.pagehandle.homeweb_userPage import HomewebUserPage


class HomewebUserBussiness():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.userpage = HomewebUserPage(self.driver)

        self.action = SeleniumAction(self.driver)

    def edit_user(self,name,englishname,wxname,facebookname):

        if name != '':

            self.action.sendkeys_ele(
                self.userpage.getelement_inputname(),name
            )

        if englishname != '':

            self.action.sendkeys_ele(
                self.userpage.getelement_inputEnglishname(),englishname
            )

        if wxname != '':

            self.action.sendkeys_ele(
                self.userpage.getelement_inputwxname(),wxname
            )

        if facebookname != '':

            self.action.sendkeys_ele(
                self.userpage.getelement_inputfacebookname(),facebookname
            )
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

        self.userpage.getelement_usereditbtn().click()

