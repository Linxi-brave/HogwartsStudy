import os
import time
import urllib

import requests
import zxing
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from testing_my_selenium_PO.pagehandle.homeweb_activityPage import HomewebBasePage

from testing_my_selenium_PO.base.seleniumAction import SeleniumAction

from util.get_tklogintoken import Teamkitlogintoken
from util.handle_time import timeN


class HomewebBaseBussiness():

    def __init__(self,driver:WebDriver):
        self.driver =driver
        self.actionEle = SeleniumAction(self.driver)
        self.homebasePage = HomewebBasePage(self.driver)

    def toLoginUrl(self):

        imgurlEle = self.homebasePage.getele_imgurl()

        # 获取图片地址
        url = self.actionEle.get_elementattribute(imgurlEle,"src")

        # 保存图片到指定路径
        if url != None:
            filename = "qcode.img"

            # 保存图片数据
            data = urllib.request.urlopen(imgurlEle).read()
            filepath = os.path.join(os.getcwd() + 'img')
            file = filepath + filename
            f = open( file, 'wb')
            f.write(data)
            f.close()

        # 获取图片内容
        def getcode(codelist):
            for value in codelist:
                if value.find("pcQrCodeLogin://") == 0:
                    codeStr = value
                    code = codeStr[16:]
                    return code
                    break

        reader = zxing.BarCodeReader()
        barcode = reader.decode(file)
        codelist = str(barcode).split("'")
        query = getcode(codelist)

        def qrcodelogin(query,type):
            ''' Teamkit 登录函数'''
            header = Teamkitlogintoken().getMerloginHeader()[0] # 获取Teamkit登录的header
            urlmemberinfo = "https://dnapp.bitkinetic.com/api/v5/user/qrcodelogin"

            body = {
                'query':query,
                'type':type
            }
            response = requests.post(urlmemberinfo,data=body,header=header)

        qrcodelogin(query,'status')
        qrcodelogin(query,'login')

    def addActivity(self,acttitle='',actbegintime='',actcontent = ''):

        if acttitle != '':
            # 输入活动标题
            addactinput = self.homebasePage.getele_addacttitleinput()

            self.actionEle.sendkeys_ele(addactinput,acttitle)

        if actbegintime != '':
            # 输入活动时间
            addacttimeinput = self.homebasePage.getele_addactbegintimeinput()
            actbegintimeStr = timeN(7)

            self.actionEle.sendkeys_ele(addacttimeinput,str(actbegintimeStr))
            btns = self.driver.find_elements_by_xpath("//div[@class='el-form-item bottomBtn']//button")
            time.sleep(1)
            btns[1].click()

        if actcontent != '':
            self.actionEle.swipeup()
            # 输入活动内容
            addcontentinput = self.homebasePage.getele_addactcontentinput()

            self.actionEle.sendkeys_ele(addcontentinput,actcontent)

        self.driver.find_element(By.XPATH,'//span[text()="立即发布"]').click()
        print('true')

        # $x('//div[@class="el-form-item__content"]//span[text()="立即发布"]')
        self.driver.find_element(By.XPATH,'//div[@class="el-form-item__content"]//span[text()="立即发布"]').click()
        self.actionEle.click_ele(self.homebasePage.getele_submitbycss())

        print("true")


