from datetime import datetime

import pytest

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase
from testing_my_selenium_PO.business.homeweb_promiseBussiness import HomewebPromiseBussiness
from util.handle_time import timenow


class TestcaseHomewebPromise(SeleniumBase):

    def setup(self):

        self.promisebussiness = HomewebPromiseBussiness(self.driver)


    def testcase_createpromise(self):

        pass

    def testcase_promiselist(self):

        self.driver.get('https://home.bitkinetic.com/promise')

        data = self.promisebussiness.getdata_listtitle()

        pytest.assume(str(timenow()) in data["title"][0])

