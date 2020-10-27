from testing_my_selenium_PO.base.seleniumFindelement import FindElement


class HomewebAnnouncePage():

    def __init__(self,driver):
        self.driver =driver
        self.findment = FindElement(self.driver)

    def goto_createpage(self):

        self.findment.get_element('announcecreatepage').click()

    def getelement_antitleinput(self):

        return self.findment.get_element('antitleinput')

    def getelement_aninput(self):

        return self.findment.get_element('aninput')

    def getelement_createbtn(self):

        return self.findment.get_element('createbtn')


    def geteles_listanncontext(self):

        return self.findment.get_element('listanncontext')

    def geteles_listanntitle(self):

        return self.findment.get_element('listanntitle')
