from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.add_member_page import AddMemberage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    '''主界面'''



    def goto_add_member_page(self):
        ''' 从首页进入添加联系人界面'''

        eles = self.finds(By.XPATH,"//div[@class='index_service_cnt js_service_list']//a")
        eles[0].click()

        return AddMemberage(self.driver)

    def goto_memberlist_page(self):
        '''从首页进入通讯录界面'''

        self.find(By.ID,"menu_contacts").click()
        return AddMemberage(self.driver)


