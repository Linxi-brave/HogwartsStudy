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

    def get_element_xztdbtn(self):
        ''' 获取新增团队按钮'''
        return self.findelement.get_element("xztdbtn")

    def get_element_ssyyinput(self):
        '''获取搜索应用输入框'''
        return self.findelement.get_element("ssyyinput")

    def get_element_xzteamkitspan(self):
        '''获取选择Teamkit span'''
        return self.findelement.get_element("xzteamkitspan")

    def get_element_xzuserspaninput(self):
        '''获取选择用户输入框'''
        return self.findelement.get_element("xzuserspaninput")
    def get_elements_xzuserspan(self):

        '''获取选择用户列表'''
        return self.findelement.get_element("xzuserspaneles")

    def get_element_userspan(self,phone):
        '''从选择用户列表中获取某个用户'''
        # 这里如果调用封装的FindElement则无法将参数为动态获取，如果没有调用封装则没有写日志
        # return self.findelement.get_childelement(self.get_elements_xzuserspan(),)
        return self.get_elements_xzuserspan().find_element_by_link_text(phone)

    def get_element_teamnameinput(self):
        '''获取团队名称输入框'''
        return self.findelement.get_element("teamnameinput")

    def get_element_companyinput(self):
        '''获取公司名称输入框'''

        return self.findelement.get_element("companyinput")

    def get_element_accpetbtn(self):
        '''获取确定按钮'''

        return self.findelement.get_element("acceptbtn")

    def get_element_cancelbtnbtn(self):
        '''获取取消按钮'''

        return self.findelement.get_element("cancelbtn")

