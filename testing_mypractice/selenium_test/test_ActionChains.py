import shelve


import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from testing_mypractice.selenium_test.seleniumbase import SeleniumBase
'''
Action 
ActionChains : 执行PC端的点击、双击、右击、拖动等操作
TouchActions : 模拟PC端和移动端的点击、双击、滑动、拖动等多手势操作
ActionChains : 调用的时候不会马上执行，而是放在队列中，当执行 action.perform() 才执行操作
ActionChains 只是针对PC端的操作，对H5的操作可能无用，对H5的可以使用ActionChains 
            
'''
class TestActionChains(SeleniumBase):
    # def setup(self):
    #     self.option = webdriver.ChromeOptions()
    #     self.option.add_experimental_option('w3c',False)
    #
    #     self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
    #     self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)
    #     self.driver.implicitly_wait(2)
    #     self.driver.maximize_window()
    #
    # def teardown(self):
    #     self.driver.quit()

    @pytest.mark.skip
    def testcase_click(self):
        self.driver.get("https://juejin.im/")
        element_click = self.driver.find_elements_by_xpath('//*[@id="juejin"]/div[2]/div/header/div/a')
        element_rightclick = self.driver.find_elements_by_xpath('//*[@id="juejin"]/div[2]/div/header/div/a')
        element_doubleclick = self.driver.find_elements_by_xpath('//*[@id="juejin"]/div[2]/div/header/div/a')

        # 使用 action 进行单击、右击、双击
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()
    @pytest.mark.skip
    def testcase_movetoelement(self):
        # 光标移动到某个元素上面
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    @pytest.mark.skip
    def testcase_dragdrop(self):
        # 将元素1拖到元素2然后释放
        self.driver.get("https://www.baidu.com")
        ele1 = self.driver.find_element_by_link_text("设置")
        ele2 = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2)
        action.perform()

    @pytest.mark.skip
    def test_keys(self):
        # 模拟键盘操作
        self.driver.get("https://www.baidu.com")
        inputele = self.driver.find_element_by_xpath('//*[@id="kw"]')
        inputele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACKSPACE).pause(1)
        action.perform()

    @pytest.mark.skip
    def test_touchaction_scrollbottom(self, ):
        # 使用 TouchActions 实现界面的滑动到底端
        self.driver.get("https://www.baidu.com")
        inputele = self.driver.find_element_by_xpath('//*[@id="kw"]')
        searchele = self.driver.find_element_by_id("su")
        inputele.send_keys("username")
        action = TouchActions(self.driver)
        action.tap(searchele)
        action.perform()
        action.scroll_from_element(inputele,0,10000).perform()
        sleep(6)
    @pytest.mark.skip
    def test_form(self):
        # 表单相关的操作
        self.driver.get("https://testerhome.com/account/sign_in")
        userinput = self.driver.find_elements_by_xpath('//*[@id="user_login"]')
        pwdinput = self.driver.find_elements_by_xpath('//*[@id="user_password"]')
        submitbtn = self.driver.find_elements_by_xpath('//*[@id="new_user"]/div[4]/input')

        userinput.send_keys("111")
        pwdinput.send_keys("222")
        submitbtn.click()

    @pytest.mark.skip
    def test_addteam(self):
        self.loginurl = "https://apiadmin.bitkinetic.com/auto?wx=mattkay"
        self.driver.get(self.loginurl)

        self.driver.implicitly_wait(5)

        self.driver.get("https://admin.bitkinetic.com/user")

        self.driver.implicitly_wait(10)

        yhgllist = self.driver.find_elements_by_class_name("el-table__row")

        for i in yhgllist:
            print(i.text)



    @pytest.mark.skip
    def test_form_xztd(self):
        try:
            print("测试新增团队")
            self.loginurl = "https://apiadmin.bitkinetic.com/auto?wx=ZhangLiYe"
            self.driver.get(self.loginurl)

            self.driver.implicitly_wait(4)

            self.driver.get("https://admin.bitkinetic.com/team")
            self.driver.implicitly_wait(2)

            xztdbtn = self.driver.find_element_by_xpath("//button[@class='el-button el-button--primary']/span") #点击新增团队
            xztdbtn.click()
            ssyyinput = self.driver.find_element_by_xpath("//input[@placeholder='搜索所属应用']").click()  # 点击输入框
            # ssyyinput.click()

            action = ActionChains(self.driver)
            action.send_keys("TeamKit").pause(4)
            action.perform()
            sleep(5)
            self.driver.implicitly_wait(5)
            # WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element(
            #     # locator=(By.XPATH, "//li[@class='el-select-dropdown__item selected hover']")
            #     # self.driver.find_element_by_xpath("//li[@class='el-select-dropdown__item selected hover']")
            #     # self.driver.find_element_by_css_selector("li[class='el-select-dropdown__item selected hover']")
            #
            # ))
            locator = (By.XPATH, '//div[@class="el-scrollbar"]//span')
            try:
                WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
                self.driver.find_element_by_xpath('//div[@class="el-scrollbar"]//span').is_clickable()
                self.driver.find_element_by_xpath('//div[@class="el-scrollbar"]//span').click()
            finally:
                self.driver.close()


            xzteamkitspan = self.driver.find_element_by_css_selector("li[class='el-select-dropdown__item selected hover']") # 选择Teamkit

            action = ActionChains(self.driver)
            action.move_to_element(xzteamkitspan)
            action.click()
            # xzteamkitspan.click()

            xzuserspaninput = self.driver.find_element_by_xpath("//input[@placeholder='搜索用户名/id/手机号']")
            xzuserspaninput.click()
            action = ActionChains(self.driver)
            action.send_keys("51").pause(2)
            action.perform()

            xzuserspaneles = self.driver.find_elements_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li")  # 选择团队长列表

            action = ActionChains(self.driver)
            action.move_to_element(xzuserspaneles[0])
            action.click()
            action.perform()

            teamnameinput = self.driver.find_element_by_xpath("//input[@placeholder='请输入团队名']")
            teamnameinput.send_keys("辉煌团队")

            companyinput = self.driver.find_element_by_xpath("//input[@placeholder='请输入名称']")
            companyinput.send_keys("平安保险团队")

            cancelbtn = self.driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small']")
            acceptbtn = self.driver.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--small']")

            acceptbtn.click()

            texteles = self.driver.find_elements_by_class_name("el-form-item__error")

            textlist = []
            for i in range(0, len(texteles) - 1):
                print(texteles[i].text)
                textlist.append(texteles[i].text)
            print(textlist)
        except Exception as e:
            print(e)
            self.driver.quit()












