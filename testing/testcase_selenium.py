import os
import shelve

import pytest
from selenium import  webdriver
class TestcaseSelenium():

    def setup(self):

        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("w3c",False)
        self.option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')

        # 控制已打开的浏览器：通过debug模式打开：　
        # $ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome -remote-debugging-port=9222
        # 备注：　　1. 启动浏览器dbug模式时需要把浏览器打开的进程先全部关闭。
        # 　　     2. 9222是默认端口，可以随意修改。但别使用已经被占用的端口。


        self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
        self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)

        self.driver.implicitly_wait(2)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def testcasegetcookie(self):

        # 获取到浏览器的cookies
        cookies = self.driver.get_cookies()
        db = shelve.open("cookies")
        db['cookies'] = cookies
        # print(db['cookies'])
        db.close()



    # @pytest.mark.skip
    def testcaseselenium(self):

        # 获取到数据库 cookie 中存储的cookie 值，并赋值到浏览器的coolkie中
        db = shelve.open("cookies")
        cookie = db['cookies']
        db.close()
        for icookie in cookie:
            self .driver.add_cookie(icookie)

        url = 'https://work.weixin.qq.com/wework_admin/frame'
        self.driver.get(url)

        # 获取【常用入口】的6个功能按钮入口，分别是 ：添加成员、导入通讯录、成员加入、消息群发、客户联系、打卡

        eles = self.driver.find_elements_by_xpath('//span[@class="index_service_cnt_item_title"]')

        # 点击导入通讯录

        eles[1].click()

        # 进入导入通讯录界面，延时3秒

        self.driver.implicitly_wait(3)

        # 导入通讯录文件
        # 通讯录文件目录：/Users/huangwenjiao/HogwartsStudy/testing/通讯录.xlsx

        file = os.getcwd() + '/通讯录.xlsx'
        self.driver.find_element_by_xpath('//input').send_keys(file)

        # 校验上传成功后界面显示 '通讯录.xlsx'
        asserttext = self.driver.find_element_by_xpath('//div[@class="ww_fileImporter_fileContainer_fileNames"]').text
        pytest.assume( asserttext == '通讯录.xlsx')







