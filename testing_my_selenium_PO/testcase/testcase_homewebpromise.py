from datetime import datetime

import allure
import pytest

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.homeweb_promiseBussiness import HomewebPromiseBussiness
from util.handle_time import timenow

@allure.feature('测试必达模块')
class TestcaseHomewebPromise(SeleniumBase):

    def setup(self):

        self.promisebussiness = HomewebPromiseBussiness(self.driver)

    @allure.feature('测试成功发布必达')
    def testcase_createpromise(self):

        pass

    @allure.story('验证必达列表数据正确性')
    def testcase_promiselist(self):

        self.driver.get('https://home.bitkinetic.com/promise')

        data = self.promisebussiness.getdata_listtitle()

        pytest.assume(str(timenow()) in data["title"][0])

