import pytest
import yaml

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.baseBussiness import BaseBussiness
from testing_my_selenium_PO.pagehandle.basePage import BasePage
import time
from testing_my_selenium_PO.sqldata.basepageData import BasepageData
import allure

import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
def getdata_addteam():

    file = parent_dir + "/testdata/addteam.yaml"
    with open(file,encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        data = datas['addteam']['test']
        return data


@pytest.mark.parametrize("userphone",
                         getdata_addteam())
def testgetdata(userphone):
    # print(userphone)
    print(userphone[0])





@allure.story("列表数据测试")
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

    @allure.story("用户管理列表数据校验")
    def testcaseyhgllistdata(self):

        self.driver.get("https://admin.bitkinetic.com/user")
        self.driver.implicitly_wait(3)

        # 获取UI界面上用户管理列表的数据
        uilistdata = self.bussiness.get_yhgllistdata()

        # 获取通过数据库获得的用户管理列表的数据
        sqllistdata = self.sqldata.sql_yhgllistdata()

        # 校验列表的数据
        for x in (0,1):

            with allure.step("校验用户管理列表数据中的用户ID,数据序号:" + str(x)):
                pytest.assume(str(uilistdata[x][0]) == str(sqllistdata[x][0]))

            with allure.step("校验用户管理列表数据中的用户手机号,数据序号:" + str(x)):
                pytest.assume(str(uilistdata[x][1]) == str(sqllistdata[x][1]))

            with allure.step("校验用户管理列表数据中的用户昵称，数据序号:" + str(x)):
                pytest.assume(str(uilistdata[x][2]) == str(sqllistdata[x][2]))


    @pytest.mark.parametrize("userphone,company,app,teamname",
                             getdata_addteam())
    @pytest.mark.skip
    def test_addnewteam(self,userphone,company,app,teamname):

        def starturl():
            '''每次都要重新刷新'''
            self.driver.get("https://admin.bitkinetic.com/team")
            self.driver.implicitly_wait(3)

        def getallerttext():
            '''获取校验值'''
            allerttext = self.bussiness.asserttext_addnewteam()
            return allerttext

        with allure.step("校验所有输入框不输入，点击确定按钮"):

            starturl()

            self.bussiness.add_newteam(submit="Yes")

            pytest.assume(["请搜索并选择 应用","请搜索并选择 用户","请输入 团队名","请输入 所属公司"] == getallerttext())

        with allure.step("校验输入应用，点击确定按钮"):
            starturl()

            self.bussiness.add_newteam(submit="Yes",appname="Teamkit")

            pytest.assume(["请搜索并选择 用户","请输入 团队名","请输入 所属公司"] == getallerttext())

        with allure.step("校验输入用户手机号，点击确定按钮"):

            starturl()

            self.bussiness.add_newteam(submit="Yes",userphone=userphone)

            pytest.assume(["请搜索并选择 应用","请输入 团队名","请输入 所属公司"] == getallerttext())

        with allure.step("校验输入所属公司，点击确定按钮"):

            self.bussiness.add_newteam(submit="Yes",companyname=company)

            asserttext = getallerttext()

            pytest.assume("请输入 团队名" in asserttext)
            pytest.assume("请搜索并选择 应用" in asserttext)
            pytest.assume("请搜索并选择 应用" in asserttext)

        with allure.step("校验全部上传点击确定，成功创建团队"):

            self.bussiness.add_newteam(submit="Yes",appname= app,userphone= userphone,
                                       teamname= teamname,companyname=company)














