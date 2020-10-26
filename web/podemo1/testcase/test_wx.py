from web.podemo1.page.base_page import BasePage
from web.podemo1.page.main_page import MainPage


class TestWX():

    def setup(self):
        self.main = MainPage(driver=None)

    def testcase_addmember(self):

        username = 'aaa'
        account = '15088132074'
        phonernum = '15088132074'

        # 进入添加联系人界面,进行添加联系人
        addmember = self.main.goto_add_member_page()

        addmember.add_member(username,account,phonernum)
        assert username in  addmember.get_member()


    def testcase_addmember2(self):

        # 点击通讯录，进入通讯录界面
        memberlist = self.main.goto_memberlist_page()

        memberlist.click_addmember()

