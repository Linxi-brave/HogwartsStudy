
from testing_my_selenium_PO.base.seleniumFindelement import FindElement
from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
class HomewebBasePage():
    def __init__(self,driver):
        self.driver = driver
        self.findelemnt = FindElement(self.driver)

        self.action = SeleniumAction(self.driver)

    def getele_imgurl(self):

         return self.findelemnt.get_element("imgurl")

    def getele_teamkitlogo(self):

        return self.findelemnt.get_element("teamkitlogo")


    def gettext_teamkitlogo(self):
        '''获取定位值'''
        return self.action.get_elementtext(self.getele_teamkitlogo())

    def getele_addactbtn(self):

        return self.findelemnt.get_element('addactbtn')

    def getele_addacttitleinput(self):

        return self.findelemnt.get_element("addtitleinput")

    def getele_addactbegintimeinput(self):

        return self.findelemnt.get_element('addactbegintimeinput')

    def getele_addactcontentinput(self):

        return self.findelemnt.get_element('addactinput')

    def getele_submitactbtn(self):

        return self.findelemnt.get_element('submitactbtn')

