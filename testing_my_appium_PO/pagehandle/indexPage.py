from testing_my_appium_PO.base.appiumBase import AppiumBase


class IndexPage(AppiumBase):

    def setup(self):

        pass

    def teawdown(self):

        pass


    def test_search(self):

        homesearch = self.get_element('homesearch')