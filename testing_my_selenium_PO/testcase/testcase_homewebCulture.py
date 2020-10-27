import os

import pytest
import yaml

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.homeweb_cultureBussiness import HomewebCultureBussiness

parent_dir = os.path.abspath(os.path.join(os.getcwd(),'../..'))

file = parent_dir + '/testdata/testdata.yaml'

def get_culturedata():

    with open(file,encoding='utf-8') as f:

        datas = yaml.safe_load(f)

        data = datas['createculture']['testdata']

        caseid = datas['createculture']['caseid']

        return data,caseid

def get_culturelink():

    with open(file,encoding='utf-8') as f:

        datas = yaml.safe_load(f)

        data = datas['createculturelink']['testdata']

        caseid = datas['createculturelink']['caseid']

        return data,caseid


class TestcaseHomewebCulture(SeleniumBase):

    def setup(self):

        self.bussiness = HomewebCultureBussiness(self.driver)


    @pytest.mark.parametrize('title,context',get_culturedata()[0],
                             ids = get_culturedata()[1]
                             )
    def testcase_createculture(self,title,context):
        self.driver.get('https://home.bitkinetic.com/find/publishfind')

        self.bussiness.create_culture(titleinput= title,contextinput= context)

    @pytest.mark.parametrize('link',get_culturelink()[0],
                             ids = get_culturelink()[1])
    def testcase_createlinkculture(self,link):
        self.driver.get('https://home.bitkinetic.com/find/publishfind')
        self.bussiness.create_linkculture(linkinput= link )