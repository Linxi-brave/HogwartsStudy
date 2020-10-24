

import  os

import pytest
import yaml

from util_.selenium_base import SeleniumBase
from testing_my_selenium_PO.business.homeweb_baseBussiness import HomewebBaseBussiness

parent_dir = os.path.abspath(os.path.join(os.getcwd(),"../.."))
def get_addActivitydata():
    # 获得发布活动的测试数据
    file = parent_dir + '/testdata/testdata.yaml'

    with open(file,encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        data = datas['addactivitydata']['testdata']
        caseid = datas['addactivitydata']['caseid']
        return data,caseid

class TestcaseHomeweb(SeleniumBase):

    def __init__(self,driver):
        self.driver = driver
        self.bussiness = HomewebBaseBussiness(self.driver)


    @pytest.mark.parametrize(
        "title,begintime,context,asserttext",get_addActivitydata()[0],
        ids = get_addActivitydata()[1]
    )
    def testcaseAddActivity(self,title,begintime,context,asserttext):

        # 打开界面
        self.driver.get("")
        #
        self.bussiness.addActivity(acttitle=title,actbegintime=begintime,actcontent=context)

        # pytest.assume(asserttext == )