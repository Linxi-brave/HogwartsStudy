from testing_my_selenium_PO.pagehandle.basePage import BasePage
from testing_my_selenium_PO.base.seleniumAction import SeleniumAction
class BaseBussiness():

    def __init__(self,driver):
        self.driver = driver
        self.actionElement = SeleniumAction(self.driver)
        self.basePage = BasePage(self.driver)


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
        print(respectlist)
        return respectlist


    def add_newteam(self,appname = None,userphone=None,teamname=None,companyname=None,submit = "Yes"):
        '''
        封装新增团队功能 ，不传入对应参数则对应不输入
        :param submit: 为 Yes 则确定提交，为 No 则取消提交
        '''
        # 点击创建团队按钮
        self.basePage.get_element_xztdbtn().click()
        # 输入搜索应用输入框 ,输入内容为 Teamkit,出现下拉选择框
        if appname != None:
            self.actionElement.actionchain_keys(self.basePage.get_element_xzteamkitspan(),appname)
            # 选择 Teamkit 应用并点击

            ele = self.basePage.get_element_xzteamkitspan()
            self.actionElement.actionchain_movetoelement(ele)
            self.actionElement.actoinchain_click()

        # 输入 团队长输入框，输入内容为 参数userphone ，出现下拉选择框
        if userphone != None:
            self.actionElement.actionchain_keys(self.basePage.get_element_xzuserspaninput(),userphone)
            # 从下拉选择框中选择参数为 phone 的span ,并点击选中
            ele = self.basePage.get_element_userspan(userphone)
            self.actionElement.actionchain_movetoelement(ele)
            self.actionElement.actoinchain_click()

        # 输入团队名称输入框，输入参数为 teamname
        if teamname!= None:
            self.basePage.get_element_teamnameinput().send_keys(teamname)
        # 输入公司名称输入框，输入参数为 companyname
        if companyname != None:
            self.basePage.get_element_companyinput().send_keys(companyname)
        if submit == "Yes":
            self.basePage.get_element_accpetbtn().click()
        else:
            self.basePage.get_element_cancelbtnbtn().click()

    def asserttext_addnewteam(self):
        '''获取新增团队框，输入框未输入内容时，校验文案'''
        textlist = []
        for i in range(0,len(textlist) - 1):
            textlist.append(textlist[i].text)
        return textlist
