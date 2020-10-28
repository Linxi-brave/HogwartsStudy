import os

import allure
import pytest
import yaml

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.homeweb_reportBussiness import HomewebReportBussiness

parent_dir = os.path.abspath(os.path.join(os.getcwd(),"../.."))

def get_addreportdata():

    file = parent_dir + '/testdata/testdata.yaml'

    with open(file,encoding= 'utf-8') as f:

        datas = yaml.safe_load(f)

        data = datas['creatreportdata']['testdata']

        caseid = datas['creatreportdata']['caseid']

        return data,caseid

@allure.feature('测试报告模块')
class TestcaseHomewebReport(SeleniumBase):

    def setup(self):

        self.business = HomewebReportBussiness(self.driver)


    # @pytest.mark.skip
    @pytest.mark.parametrize('sumary,plan,sale,content',get_addreportdata()[0],
                             ids = get_addreportdata()[1])
    @allure.story('验证发布报告')
    def testcase_createreport(self,sumary,plan,sale,content):

        self.business.creatReport(sumary,plan,sale,content)



