

import  os

import pytest
import yaml

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.homeweb_activityBussiness import HomewebBaseBussiness
import allure

parent_dir = os.path.abspath(os.path.join(os.getcwd(),"../.."))

def get_addActivitydata():
    # 获得发布活动的测试数据
    file = parent_dir + '/testdata/testdata.yaml'

    with open(file,encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        data = datas['addactivitydata']['testdata']
        caseid = datas['addactivitydata']['caseid']
        return data,caseid

@allure.feature('测试活动模块')
class TestcaseHomeweb(SeleniumBase):

    def setup(self):
        self.bussiness = HomewebBaseBussiness(self.driver)


    @pytest.mark.parametrize(
        "title,begintime,context,asserttext",get_addActivitydata()[0],
        ids = get_addActivitydata()[1]
    )
    @allure.story('测试成功发布活动')
    def testcaseAddActivity(self,title,begintime,context,asserttext):


        self.driver.get("https://home.bitkinetic.com/activity/activityRelease")

        print(title,begintime,context,asserttext)
        self.bussiness.addActivity(acttitle=title,actbegintime=begintime,actcontent=context)

        # pytest.assume(asserttext == )



    def testselectbtn(self):

        self.driver.get("https://home.bitkinetic.com/powerFeature")
