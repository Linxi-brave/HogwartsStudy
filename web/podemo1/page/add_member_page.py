from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
# CSS :
# id #
# classname .
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.base_page import BasePage


class AddMemberage(BasePage):

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def click_addmember(self):
        '''点击【添加成员】按钮'''
        locator = (By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)")

        def wait_for_next(x:WebDriver):
            # 反复点击【添加成员】，直到点击通过
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")   # 这里为什么要 return 这个，上一句不是已经实现了点击操作了么？
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)


    def add_member(self,username,account,phonernum):
        '''添加联系人'''

        # 输入名字输入框
        self.find(By.ID,"username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonernum)
        # 点击提交
        self.find(By.CSS_SELECTOR,".js_btn_save").click()

        checkbox = (By.CSS_SELECTOR,'ww_checkbox')
        self.wait_for_click(checkbox)
        return True



    def get_member(self,value):
        '''验证联系人'''

        total_list = []
        # 获取第一页联系人列表
        contactlist = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")

        titlelist = [element.get_attribute("title") for element in contactlist]

        print(titlelist)

        if value in titlelist:
            return True
        total_list = total_list + titlelist

        result:str = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text

        num,total = result.split('/',1)

        if int(num) == int(total):
            return False
        else:
            self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list