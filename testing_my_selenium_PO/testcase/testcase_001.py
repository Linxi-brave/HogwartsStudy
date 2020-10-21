import pytest

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.baseBussiness import BaseBussiness
from testing_my_selenium_PO.pagehandle.basePage import BasePage
import time
from testing_my_selenium_PO.sqldata.basepageData import BasepageData
class Testcase(SeleniumBase):

    def setup(self):
        self.bussiness = BaseBussiness(self.driver)
        self.basepage = BasePage(self.driver)
        self.sqldata = BasepageData()

        self.loginurl = "https://apiadmin.bitkinetic.com/auto?wx=mattkay"
        time.sleep(2)
        self.driver.get(self.loginurl)
        self.driver.implicitly_wait(4)

    @pytest.mark.skip
    def testcase001(self):
        self.driver.get("https://admin.bitkinetic.com/")
        self.driver.implicitly_wait(5)
        time.sleep(5)

        self.bussiness.Bussiness001()
        pytest.assume(self.basepage.gettitle_base() == '团队管理丨TeamKit运营系统')

        #
        # title = self.basepage.gettitle_base()
        #
        # pytest.assume(title == "这个界面")


    def testlist(self):

        self.driver.get("https://admin.bitkinetic.com/user")
        self.driver.implicitly_wait(3)
        # 获取UI界面上用户管理列表的数据
        uilistdata = self.bussiness.get_yhgllistdata()

        # 获取通过数据库获得的用户管理列表的数据
        sqllistdata = self.sqldata.sql_yhgllistdata()

        # 校验列表的数据
        for x in (0,8):
            for y in (0,3):
                print("----x----")
                print(x,y)
                print(uilistdata[x][y])
                print(sqllistdata[x][y])
                pytest.assume(uilistdata[x][y] == sqllistdata[x][y])



        # eles = self.driver.find_elements_by_class_name("el-table__row")
        # list = []
        # for i in eles:
        #     list.append(i.text)





        # print(self.bussiness.get_yhgllistdata())



