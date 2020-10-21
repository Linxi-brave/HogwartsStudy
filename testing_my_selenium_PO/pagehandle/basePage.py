from testing_my_selenium_PO.base.seleniumFindelement import FindElement
from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.findelement = FindElement(self.driver)
        self.actionElement = SeleniumAction(self.driver)

    def get_element_zhzxspan(self):

        return self.findelement.get_element("zhzxspan")

    def get_element_tkspan(self):

        return self.findelement.get_element("tkspan")

    def get_element_tdglspan(self):

        return self.findelement.get_element("tdglspan")


    def click_element_zhzxspan(self):

        self.actionElement.click_ele(self.get_element_zhzxspan())

    def click_element_tkspan(self):

        self.actionElement.click_ele(self.get_element_tkspan())

    def click_element_tdglspan(self):

        self.actionElement.click_ele(self.get_element_tdglspan())

    def getvalue_element(self):

        return self.actionElement.get_elementtext(self.get_element())

    def gettitle_base(self):

        return self.actionElement.get_title()


    def geteles_yhgllist(self):
        '''获取用户管理列表数据的元素，为element list 形式'''

        eles = self.findelement.get_element("yhgllist")

        return eles

    def getvalue_yhgllist(self):
        '''获取用户管理列表的数据'''

        yhgllistdata = []
        for i in self.geteles_yhgllist():
            data = self.actionElement.get_elementtext(i)
            yhgllistdata.append(data)

        return yhgllistdata

