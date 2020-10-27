from selenium.webdriver.remote.webdriver import WebDriver

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.pagehandle.homeweb_promisePage import HomewebPromisePage

from util.handle_time import timeN

class HomewebPromiseBussiness():

    def __init__(self,driver:WebDriver):

        self.driver = driver

        self.promisepage = HomewebPromisePage(self.driver)

        self.action = SeleniumAction(self.driver)



    def create_promise(self,title,content):

        if title != None:

            self.action.sendkeys_ele(self.promisepage.getelement_promisetitleinput(),title)

        if content != None:

            self.action.sendkeys_ele(
                self.promisepage.getelement_promiseinput(),content
            )

        self.action.click_ele(self.promisepage.getlabel1().click())

        self.action.click_ele(self.promisepage.getlabel2().click())

        self.action.sendkeys_ele(

            self.promisepage.getelement_actbegintime(),timeN(7)
        )

        self.action.click_ele(self.promisepage.getelement_creatbtn1())

        self.action.click_ele(self.promisepage.getelement_createbtn2())


    def  getdata_listtitle(self):

        eles = self.promisepage.geteles_listpromisetitle()

        titlelist = []

        for i in eles:

            titlelist.append(self.action.get_elementtext(i))
        listdata = {'title':titlelist}

        return listdata


