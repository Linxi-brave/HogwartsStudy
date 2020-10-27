from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
from testing_my_selenium_PO.base.seleniumFindelement import FindElement


class HomewebPromisePage():

    def __init__(self,driver):

        self.driver = driver

        self.findelement = FindElement(self.driver)

        self.action = SeleniumAction(self.driver)

    def getelement_createpromisebtn(self):

        return self.findelement.get_element('createpromisebtn')

    def getelement_promisetitleinput(self):

        return self.findelement.get_element('promisetitleinput')

    def getelement_promiseinput(self):

        return self.findelement.get_element('promiseinput')

    def getlabel1(self):

        return self.findelement.get_element('label1')

    def getlabel2(self):

        return self.findelement.get_element('label2')

    def getelement_actbegintime(self):

        return self.findelement.get_element('actbegintime')

    def getelement_promisepeople(self):

        return self.findelement.get_element('promisepeople')

    def getelement_sendpeoplebtn(self):

        return self.findelement.get_element('sendpeoplebt')

    def getelement_creatbtn1(self):

        return self.findelement.get_element('creatbtn1')

    def getelement_createbtn2(self):

        return self.findelement.get_element('createbtn2')

    def geteles_listpromisetitle(self):

        return self.findelement.get_elements('listpromisetitle')

