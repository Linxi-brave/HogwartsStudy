from time import sleep

from testing_my_selenium_PO.base.seleniumBase import SeleniumBase


class TestcaseYamaxun(SeleniumBase):

    def test01(self):

        self.driver.get('https://www.amazon.com/Conair-Double-Ceramic-Curling-1-inch/dp/B07CKKGR83/ref=sr_1_5?dchild=1&keywords=hair+curling+iron&qid=1603785511&sr=8-5')
        self.driver.implicitly_wait(4)

        sleep(4)

