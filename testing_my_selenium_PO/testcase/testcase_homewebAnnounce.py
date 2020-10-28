import os

import pytest
import yaml
import allure
from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.homeweb_announceBussiness import HomewebAnnounceBussiness
from util.handle_time import timenow, timeday
import allure

parent_dir = os.path.abspath(os.path.join(os.getcwd(),"../.."))

def get_announcedata():

    file = parent_dir + '/testdata/testdata.yaml'

    with open(file,encoding='utf-8') as f:

        datas = yaml.safe_load(f)

        data = datas['createannounce']['testdata']

        caseid = datas['createannounce']['caseid']

        return data,caseid

@allure.feature('测试公告模块')
class TestcaseHomewebAnnounce(SeleniumBase):

    def setup(self):

        self.anbussiness = HomewebAnnounceBussiness(self.driver)


    @pytest.mark.parametrize('mtitle,mcontent',
                             get_announcedata()[0],ids = get_announcedata()[1]
                             )
    # @pytest.mark.
    @allure.story('测试成功发布公告')
    def testcase_createannounce(self,mtitle,mcontent):

        # self.driver.get('https://home.bitkinetic.com/announcement')

        # self.anbussiness.goto_createpage()

        self.driver.get('https://home.bitkinetic.com/announcement/publishAnnounceMent')

        self.anbussiness.createannounce(title=mtitle,content=mcontent)




    @allure.story("验证公告列表数据正确性")
    def testcase_list(self):

        self.driver.get('https://home.bitkinetic.com/announcement')

        listdata = self.anbussiness.get_listdata()

        # pytest.assume(str(timeday()) in str(listdata["context"][0]))

        pytest.assume('2020-10-26' in str(listdata["context"][0]))




