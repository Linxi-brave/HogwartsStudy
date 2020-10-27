from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.pagehandle.homeweb_announcePage import HomewebAnnouncePage
from util.handle_time import timenow


class HomewebAnnounceBussiness():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.action = SeleniumAction(self.driver)

        self.anpage = HomewebAnnouncePage(self.driver)

    def goto_createpage(self):

        self.anpage.goto_createpage()

    def createannounce(self,title,content):

        sleep(2)

        if title != '':
            time = timenow()
            self.action.sendkeys_ele(
                self.anpage.getelement_antitleinput(),title
            )

        if content != '':
            self.action.sendkeys_ele(
                self.anpage.getelement_aninput(),content + time
            )

        # loctor = (By.XPATH,"//button[@class='el-button handlebtn publish el-button--primary']/span")
        #
        # self.action.click_ele_wait(loctor,self.anpage.getelement_createbtn())
        #

        btn = self.driver.find_element_by_xpath("//form//button[@class='el-button handlebtn publish el-button--primary']/span")
        btn.click()

        sleep(2)
        self.action.click_ele(self.anpage.getelement_createbtn())
        print("1111")
        # self.action.actionchain_movetoelement(
        #     self.anpage.getelement_createbtn()
        # )
        #
        # self.action.actionchain_doubleclick(
        #     self.anpage.getelement_createbtn()
        # )

        # self.driver.find_element(loctor).click()
        # self.action.click_ele_try(loctor)


    def get_listdata(self):

        eles = self.anpage.geteles_listanntitle()

        contexteles = self.anpage.geteles_listanncontext()

        titlelist = []
        contextlist = []

        for i in eles:

            titlelist.append(self.action.get_elementtext(i))

        for i in contexteles:

            contextlist.append(self.action.get_elementtext(i))

        listdata = {'title':titlelist,'context':contextlist}

        return listdata


