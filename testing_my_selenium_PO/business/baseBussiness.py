from testing_my_selenium_PO.pagehandle.basePage import BasePage
class BaseBussiness():

    def __init__(self,driver):
        self.driver = driver
        self.basePage = BasePage(self.driver)

    def Bussiness001(self):
        self.basePage.click_element_zhzxspan()
        self.basePage.click_element_tkspan()
        self.basePage.click_element_tdglspan()

    def get_yhgllistdata(self):
        ''' 获取用户管理列表的数据，并以二维数组形式返回'''
        list = self.basePage.getvalue_yhgllist()

        slist = []
        for ili in list:
            ili = ili.split(',')
            slist.append(ili)
        respectlist = []
        for i in range(0,len(slist) - 1):
            respectli = slist[i][0].split('\n')
            respectlist.append(respectli)
        return respectlist