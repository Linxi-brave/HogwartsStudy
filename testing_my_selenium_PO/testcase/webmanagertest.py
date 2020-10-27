# coding=utf-8
import sys
sys.path.append('/Users/huangwenjiao/TestingScript/seleniumTestcase')
import traceback

from selenium import webdriver
# from ..log.user_log import UserLog
from  ..base.teamkitlogintoken import Teamkitlogintoken
from ..base.find_element import FindElement
import unittest
import os
import urllib
import zxing
import requests
import time
import  datetime


Teamkitlogin = Teamkitlogintoken()
Teamkitlogin.url = "https://dnapp.bitkinetic.com/api/v5/login/mplogin"
Teamkitlogin.body = {
    "zoneNum": "86",
    "phone": "15088132074",
    "password": "123456"
}

#扫码登录
#type = status ,扫描尝试登录 ； type =login，进行登录
def qrcodelogin(query,type):

    header = Teamkitlogin.getMerloginHeader()[0]
    urlmemberinfo = "https://dnapp.bitkinetic.com/api/v5/user/qrcodelogin"

    body = {
	"query": query,
	"type": type
    }

    response = requests.post(urlmemberinfo,data=body,headers=header).json()

def timeN(n):
    time = datetime.datetime.now() + datetime.timedelta(days=int(n))
    timeN = time.strftime("%Y-%m-%d %H:%M:%S")
    return timeN

#管理员登录测试
class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        #selenium 调用，浏览器默认参数
        cls.option = webdriver.ChromeOptions()
        # 禁用JavaScript
        cls.option.add_argument("--disable-javascript")
        # 谷歌文档提到需要加上这个属性来规避bug
        cls.option.add_argument('--disable-gpu')
        cls.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        cls.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
        cls.driver = webdriver.Chrome(options=cls.option,executable_path=cls.path)
        cls.url = "https://home.bitkinetic.com"
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.getElement = FindElement(driver=cls.driver)
        cls.driver.implicitly_wait(3)



    def setUp(self):
        self.logger.info("this is chrome")

        self.findElement = FindElement(self.driver)

    def tearDown(self):
        if sys.exc_info()[0]:
            for method_name, error in self._outcome.errors:
                if error:
                    case_name = self._testMethodName
                    self.findElement.savescreen(case_name)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.quit() #driver.close只是关闭，并不是完全关闭

    def test_001_login(self):
        time.sleep(2)
        self.img_url = self.driver.find_element_by_xpath("// *[ @ alt = '二维码']")
        time.sleep(2)
        self.relimg_ulr = self.img_url.get_attribute("src")
        # 保存图片到指定路径
        if self.relimg_ulr != None:
            filename = 'qcode.jpg'
            # 保存图片数据
            data = urllib.request.urlopen(self.relimg_ulr).read()
            filepath = os.path.join(os.getcwd() + 'img' )
            f = open(filepath + filename, 'wb')
            f.write(data)
            f.close()

        reader = zxing.BarCodeReader()
        barcode = reader.decode("/Users/huangwenjiao/TestingScript/AppiumTestcase/qcode.jpg")
        codelist = str(barcode).split("'")

        def getcode(codelist):
            for value in codelist:
                if value.find("pcQrCodeLogin://") == 0:
                    codeStr = value
                    code = codeStr[16:]
                    return code
                    break
        query = getcode(codelist)
        qrcodelogin(query,"status")
        qrcodelogin(query, "login")

        teamkit = self.getElement.get_element("xpath","//*[@id='app']/div/header/h1/span")
        self.logger.info(teamkit.text)
        if self.assertEqual(teamkit.text,"TeamKit"):
            self.logger.info("登录成功！")

        time.sleep(5)

    #封装点击团队办公
    def clickteam(self):
        try:
            teambutton = self.getElement.get_element("xpath","//*[@id='app']/div/nav/div/div[2]/div/span") #点击团队办公
            time.sleep(2)
            teambutton.click()
            self.logger.info("当前在团队办公模块")
            # self.asserttitle("活动 | TeamKit")
        except:
            self.logger.info("团队办公按钮点击失败")

    #活动
    def clickacthref(self):
        try:
            activityhref = self.getElement.get_element("xpath","//*[@id='app']/div/nav/div/div[2]/ul/li[1]/a")
            time.sleep(2)
            activityhref.click()
            self.asserttitle("活动 | TeamKit")
        except:
            self.logger.info("活动按钮点击失败")
        # self.assertEqual(gettitle,"活动 | TeamKit")
    def test_002_act(self):
        self.clickteam()
        self.clickacthref()
    #发布活动
    def test_002_act_create_001(self):
        # self.clickacthref()
        self.findElement.get_element("className","mico-add").click()
        #点击创建活动
        self.findElement.get_element("xpath","//*[@id='activityRelease']/section/article/form/div[2]/div/ul/li[1]") #点击活动类型
        time.sleep(3)
        titleinput = self.driver.find_element_by_xpath("//input[@placeholder='输入活动标题（20字符以内）']")
        time.sleep(3)
        titleinput.send_keys("类型为活动的活动")
        time.sleep(3)
        actbegintime = self.driver.find_element_by_xpath("//input[@placeholder='设置活动开始时间']")
        time.sleep(3)
        actbegintimeStr = timeN(7)
        actbegintime.send_keys(str(actbegintimeStr))
        time.sleep(3)
        actinput = self.driver.find_element_by_xpath("//div[@data-placeholder='请输入活动内容']")
        time.sleep(3)
        actinput.send_keys("1111")
        #"//form[@id='loginForm']/input[1]")
        time.sleep(3)
        button = self.driver.find_element_by_xpath("//*[@id='activityRelease']/section/article/form/div[13]/div/button[2]")
        time.sleep(4)
        button.click()
        self.logger.info("发布类型为活动的活动成功")

    def test_002_act_create_002(self):
        # self.clickacthref()
        self.findElement.get_element("className", "mico-add").click()

        #创建类型为培训的活动
        btns = self.findElement.get_element("xpaths",
                                     "//*[@id='activityRelease']/section/article/form/div[2]/div/ul/li")  # 点击培训类型
        btns[1].click()
        time.sleep(3)
        titleinput = self.driver.find_element_by_xpath("//input[@placeholder='输入活动标题（20字符以内）']")
        time.sleep(3)
        titleinput.send_keys("类型为培训的活动")
        time.sleep(3)
        actbegintime = self.driver.find_element_by_xpath("//input[@placeholder='设置活动开始时间']")
        time.sleep(3)
        actbegintimeStr = timeN(7)
        actbegintime.send_keys(str(actbegintimeStr))
        time.sleep(3)
        actinput = self.driver.find_element_by_xpath("//div[@data-placeholder='请输入活动内容']")
        time.sleep(3)
        actinput.send_keys("1111")
        time.sleep(3)
        button = self.driver.find_element_by_xpath(
            "//*[@id='activityRelease']/section/article/form/div[13]/div/button[2]")
        time.sleep(4)
        button.click()
        self.logger.info("发布类型为培训的活动成功")

    def test_002_act_create_003(self):
        # self.clickacthref()
        self.findElement.get_element("className", "mico-add").click()
        time.sleep(3)
        btns = self.findElement.get_element("xpaths",
                                     "//*[@id='activityRelease']/section/article/form/div[2]/div/ul/li")
        #创建类型为招募的活动
        btns[2].click()
        titleinput = self.driver.find_element_by_xpath("//input[@placeholder='输入活动标题（20字符以内）']")
        time.sleep(3)
        titleinput.send_keys("类型为招募的活动")
        time.sleep(3)
        actbegintime = self.driver.find_element_by_xpath("//input[@placeholder='设置活动开始时间']")
        time.sleep(3)
        actbegintimeStr = timeN(7)
        actbegintime.send_keys(str(actbegintimeStr))
        time.sleep(3)
        actinput = self.driver.find_element_by_xpath("//div[@data-placeholder='请输入活动内容']")
        time.sleep(3)
        actinput.send_keys("1111")
        time.sleep(3)
        button = self.driver.find_element_by_xpath(
            "//*[@id='activityRelease']/section/article/form/div[13]/div/button[2]")
        time.sleep(4)
        button.click()
        self.logger.info("发布类型为招募的活动成功")
    def test_002_act_create_004(self):
        # self.clickacthref()
        self.findElement.get_element("className", "mico-add").click()
        time.sleep(3)
        btns = self.findElement.get_element("xpaths",
                                            "//*[@id='activityRelease']/section/article/form/div[2]/div/ul/li")
        # 点击创建活动
        #创建类型为自定义的活动
        btns[3].click()
        typeinput = self.driver.find_element_by_xpath("//input[@placeholder='输入自定义类型（1～10字）']")
        time.sleep(3)
        typeinput.send_keys("自定义类型")
        time.sleep(3)
        titleinput = self.driver.find_element_by_xpath("//input[@placeholder='输入活动标题（20字符以内）']")
        titleinput.send_keys("自定义类型的活动")
        actbegintime = self.driver.find_element_by_xpath("//input[@placeholder='设置活动开始时间']")
        time.sleep(3)
        actbegintimeStr = timeN(7)
        actbegintime.send_keys(str(actbegintimeStr))
        time.sleep(3)
        actinput = self.driver.find_element_by_xpath("//div[@data-placeholder='请输入活动内容']")
        time.sleep(3)
        actinput.send_keys("1111")
        time.sleep(3)
        button = self.driver.find_element_by_xpath(
            "//*[@id='activityRelease']/section/article/form/div[13]/div/button[2]")
        time.sleep(4)
        button.click()
        self.logger.info("发布类型为自定义的活动成功")

    def test_002_act_apply_005(self):
        #查看活动列表
        activitylist = self.getElement.get_element("xpaths","//*[@id='app']/div/div/div/section[1]/div/article/ul/li")
        time.sleep(10)
        activitylist[0].click()
        #进入活动详情
        time.sleep(1)
        button = self.getElement.get_element("xpath","//*[@id='app']/div/div/div[4]/div/article/div[2]/div[2]/button[2]") #返回按钮
        button.click()  #点击去报名
        #self.getElement.get_element("xpath","//*[@id='app']/div/div/div[4]/div/article/div[2]/div[2]/button[2]").click()
        time.sleep(3)
        input = self.getElement.get_element("xpath", "//input[@placeholder='请填写信息']")
        input.send_keys("报名者姓名")
        time.sleep(3)
        self.getElement.get_element("xpath","//*[@id='app']/div/div/div[1]/div/div[3]/div/button[2]/span").click()
        time.sleep(1)
        self.logger.info("报名成功！")
        #查看报名凭证
        self.getElement.get_element("xpath","//*[@id='app']/div/div/div[2]/div/div[3]/div/button[2]/span").click()
        time.sleep(1)
        self.getElement.get_element("xpath","//*[@id='app']/div/div/div[3]/div/div[3]/div/button[1]/span").click()
        self.logger.info("查看报名凭证")
        time.sleep(5)
    def test_002_act_edit_006(self):
        # self.clickacthref()
        #查看活动列表
        activitylist = self.getElement.get_element("xpath","//*[@id='app']/div/div/div/section[1]/div/article/ul/li[1]")
        time.sleep(10)
        self.logger.info()
        activitylist.click("activitylist------" + activitylist)
        #编辑活动
        self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div[4]/div/article/div[2]/div[2]/div/button/span').click()
        #按钮
        buttons = self.getElement.get_element("xpaths","//*[@id='dropdown-menu-545']/li")
        buttons[2].click()
        time.sleep(1)
        titleinput = self.driver.find_element_by_xpath("//input[@placeholder='输入活动标题（20字符以内）']")
        actbegintime = self.driver.find_element_by_xpath("//input[@placeholder='设置活动开始时间']")
        actinput = self.driver.find_element_by_xpath("//div[@data-placeholder='请输入活动内容']")
        #进入编辑界面
        titleinput.send_keys("编辑")
        time.sleep(1)
        actbegintime.clear()
        actbegintimeStr = timeN(6)
        actbegintime.send_keys(str(actbegintimeStr))
        time.sleep(1)
        actinput.send_keys("编辑")
        # "//form[@id='loginForm']/input[1]")
        time.sleep(1)
        button = self.getElement.get_element("xpath","//*[@id='activityRelease']/section/article/form/div[13]/div/button[2]")
        time.sleep(2)
        button.click()
        time.sleep(3)
        self.logger.info("编辑活动成功")


    # #配置邮箱不行额
    # def test_002_act_manage(self):
    #     self.clickacthref()
    #
    #     self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/section/header/div/i[1]')# 点击配置
    #     time.sleep(2)
    #     #点击添加邮箱
    #     textarea = self.getElement.get_element("xpath",'//*[@id="CustomTextarea"]/article/article[1]/textarea')
    #     textarea.click()
    #     textarea.send_keys("730162062@qq.com")
    #     time.sleep(2)
    #     button = self.getElement.get_element("xpath",'//*[@id="CustomTextarea"]/article/article[2]/section/button')
    #     button.click()

        # 设置默认邮箱
        # setemailbtn = self.getElement.get_element("xpath",'//*[@id="activitySetting"]/section/article/ul/li[1]/span')
        # setemailbtn.click()
        # time.sleep(2)
        #
        # #删除邮箱
        # btn = self.getElement.get_element("xpath",'//*[@id="activitySetting"]/section/article/ul/li[1]/i')
        # btn.click()
        #
        # # 点击切换调查问卷
        # self.getElement.get_element("xpath", '//*[@id="activitySetting"]/section/article/nav/a[1]')
        # #添加调查问卷
        # textarea2 = self.getElement.get_element("xpath","//textarea*[placeholder='添加新问题']")
        # textarea2.send_keys("对培训内容的感兴趣程度?")
        # button.click()
        # #删除
        # btns = self.driver.find_elements_by_class_name("delete")
        # time.sleep()
        # btns[0].click()

    def clickapprovalhref(self):
        try:
            approvalhref = self.getElement.get_element("xpath", "//*[@id='app']/div/nav/div/div[2]/ul/li[2]/a")
            # self.getElement.get_element("link","审批")
            time.sleep(2)
            approvalhref.click()
            self.logger.info("点击审批")
            # self.asserttitle("审批 | TeamKit")
        except:
            self.logger.info("审批按钮点击失败")
    #审批-成员
    def test_003_appro_list(self):
        self.clickapprovalhref()
        time.sleep(5)
        #切换查看预约列表,从1～4分别是 未审批、已通过、已拒绝、已失效
        approval1 = self.getElement.get_element("xpath",'//*[@id="approval"]/section/section[1]/nav/article[1]')
        approval2 = self.getElement.get_element("xpath", '//*[@id="approval"]/section/section[1]/nav/article[2]')
        approval3 = self.getElement.get_element("xpath", '//*[@id="approval"]/section/section[1]/nav/article[3]')
        approval4 = self.getElement.get_element("xpath", '//*[@id="approval"]/section/section[1]/nav/article[4]')

        approval1.click()
        approval2.click()
        approval3.click()
        approval4.click()
        #保存截图

    # #审批-管理员
    # def test_003_001_managelist(self):
    #     approvallist = self.getElement.get_element("xpaths",'//*[@id="app"]/div/div/header/div/nav/p[1]')
    #     time.sleep(2)
    #     approvallist[0].click()
    #     approvallist[1].click()
    #     approvallist[2].click()


    #指定到报告模块
    def clickreport(self):
        try:
            reporthref = self.getElement.get_element("xpath","//*[@id='app']/div/nav/div/div[2]/ul/li[3]")
            time.sleep(3)
            reporthref.click()
            time.sleep(2)
            # self.asserttitle("报告 | TeamKit")
        except:
            self.logger.info("点击报告模块失败")
    #封装创建报告
    def createreport(self,reporttypebtn):
        self.clickreport()
        #创建日报
        time.sleep(2)
        createbtn = self.getElement.get_element("xpath",'//*[@id="report"]/section/article[2]/section[1]/div/div[2]/article/i[1]')
        try :
            createbtn.click()
            btn = reporttypebtn
            btn = self.getElement.get_element("xpath",btn)
            btn.click() #点击报告类型

            jobSummaryInput = self.getElement.get_element("xpath", "//textarea[@placeholder='请输入工作总结']")
            jobSummaryInput.send_keys("输入工作总结")
            jobPlanInput = self.getElement.get_element("xpath", "//textarea[@placeholder='请输入工作计划']")
            jobPlanInput.send_keys("输入工作计划")
            jobbtn = self.getElement.get_element("xpath",
                                                 "//*[@id='release']/section/article/form/div[9]/div/button[1]")
            jobbtn.click()
            self.logger.info("创建报告成功！")
            time.sleep(2)
        except :
            self.logger.info("无法创建报告")
    #我创建的报告列表,返回报告列表 ：//*[@id="report"]/section/article[2]/section[2]/a[1]
    #我管理的报告列表 ：//*[@id="report"]/section/article[1]/section[2]/a[1]
    def reportlist(self,xpaths):
        self.clickreport()
        try:
            Elements = self.getElement.get_element("xpaths",xpaths)
            return Elements
        except:
            self.logger.info("报告列表没有数据")

    #封装创建业绩报告
    def createsalereport(self,input,sinput,reporttypebutton):
        time.sleep(2)
        createbtn = self.getElement.get_element("xpath","/*[@id='report']/section/article[2]/section[1]/div/div[2]/article/i[1]")
        try:
            createbtn.click()
            btn = reporttypebutton
            self.getElement.get_element("xpath",btn).click()
            productinput = self.getElement.get_element("xpath", "//textarea[@placeholder='请输入产品名称']")
            productinput.send_keys(input)
            saleinput = self.getElement.get_element("xpath","//textarea[@placeholder='请输入成交额']")
            saleinput.send_keys(sinput)
            input = self.getElement.get_element("xpath", "//textarea[@placeholder='请输入Tianjia']")
            input.send_keys("添加的内容")
            jobbtn = self.getElement.get_element("xpath",
                                                 "//*[@id='release']/section/article/form/div[9]/div/button[1]")
            jobbtn.click()
            self.logger.info("创建业绩报告成功！")
            time.sleep(2)
        except:
            self.logger.info("无法创建报告")
    #封装修改报告-日报/周报/月报
    def editreport(self):

        self.logger.info("测试修改报告！")
        jobSummaryInput = self.getElement.get_element("xpath", "//textarea[@placeholder='请输入工作总结']")
        jobSummaryInput.send_keys("输入工作总结编辑")
        jobPlanInput = self.getElement.get_element("xpath", "//textarea[@placeholder='请输入工作计划']")
        jobPlanInput.send_keys("输入工作计划编辑")
        jobbtn = self.getElement.get_element("xpath",
                                             "//*[@id='release']/section/article/form/div[6]/div/button[1]")
        time.sleep(2)
        jobbtn.click()
        self.logger.info("修改报告成功！")
        time.sleep(2)
    #创建日报
    def test_004_01_createdayreport(self):

        btn = '//*[@id="release"]/section/article/ul/li[1]'
        self.createreport(btn)
    #创建周报
    def test_004_02_createweekreport(self):
        btn = '//*[@id="release"]/section/article/ul/li[2]'
        self.createreport(btn)
    #创建月报
    def test_004_03_createmonthreport(self):
        btn = '//*[@id="release"]/section/article/ul/li[3]'
        self.createreport(btn)
    #创建业绩报告
    def test_004_04_createsalereport(self):
        btn = '//*[@id="release"]/section/article/ul/li[4]'
        self.createsalereport("保诚保险",'1000',btn)
    #修改报告
    def test_004_05_editreport(self):
        self.clickreport()
        list = self.reportlist('//*[@id="report"]/section/article[2]/section[2]/a')
        list[0].click()
        btn = self.getElement.get_element("xpath",'//*[@id="Details"]/section/section/article[1]/article[2]/button[3]') #点击编辑报告
        time.sleep(5)
        btn.click() #点击修改报告
        self.editreport() #修改报告
    #封装删除报告
    def deletereport(self,listxpath):
        elelist =self.reportlist(listxpath)
        elelist[0].click()
        btn = self.getElement.get_element("xpath",'//*[@id="Details"]/section/section/article[1]/article[2]/button[1]')
        btn.click()#点击删除按钮
        time.sleep(2)
        btn = self.getElement.get_element("xpath",'/html/body/div[2]/div/div[3]/button[2]')
        time.sleep(2)
        btn.click()#点击确定删除按钮
    #成员查看报告已读未读情况
    def test_004_06_seereport(self):

        elelist =self.reportlist('//*[@id="report"]/section/article[2]/section[2]/a')
        elelist[0].click()
        btn = self.getElement.get_element("xpath",'//*[@id="Details"]/section/section/article[1]/article[2]/button[2]')
        time.sleep(2)
        btn.click()#点击查看报告已读未读情况
        time.sleep(2)
        btn = self.getElement.get_element("xpath",'//*[@id="Details"]/div[1]/div/div[2]/div[2]/button[2]/span')
        time.sleep(2)
        btn.click()#点击确定按钮
    #删除我创建的报告
    def test_004_07_deletecrereport(self):
        try:
            self.deletereport('//*[@id="report"]/section/article[2]/section[2]/a[1]')
        except:
            self.logger.info("删除报告失败，无法删除，没有定位到元素")
    #删除我管理的报告
    def test_004_08_deletemanareport(self):
        try:
            self.deletereport('//*[@id="report"]/section/article[1]/section[2]/a[1]').click()
        except:
            self.logger.info("删除报告失败，无法删除，没有定位到元素")
    def test_004_09_approreport(self):
        #点击查看我管理的报告，并进行批复，批复提示报错
        report = self.getElement.get_element("xpath","//*[@id='report']/section/article[1]/section[2]/a[1]")
        time.sleep(2)
        report.click()
        # textbtn = self.getElement.get_element("xpath",'//*[@id="Details"]/section/section/article[4]/article[1]')
        # textbtn.click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        popupinput = self.getElement.get_element("xpath","//textarea[@placeholder='添加批复']")
        time.sleep(2)
        popupinput.click()
        popupinput.send_keys("这是批复测试")
        self.getElement.get_element("xpath","//*[@id='Details']/section/section/article[4]/article[2]/section/button").click()
        time.sleep(2)
        self.logger.info("批复测试成功！！")

    def clickpromisehref(self):
        try:
            promisehref = self.getElement.get_element("xpath", "//*[@id='app']/div/nav/div/div[2]/ul/li[4]")
            time.sleep(2)
            promisehref.click()
            self.asserttitle("必达 | TeamKit")
        except:
            self.logger.info("点击必达失败")

    def test_005_01_createpromise(self):
        self.clickpromisehref()
        #创建必达
        self.getElement.get_element("xpath","//*[@id='app']/div/div/div/section[1]/header/div/i").click()
        time.sleep(2)
        promisetitleInput = self.getElement.get_element("xpath", "//input[@placeholder='输入必达标题（20字符以内）']")
        promisetitleInput.send_keys("必达标题")
        promiseInput = self.getElement.get_element("xpath","//textarea[@placeholder='输入必达内容']")
        promiseInput.send_keys("必达内容")
        label1 = self.getElement.get_element("xpath","//*[@id='app']/div/div/div[2]/article/form/div[4]/div/label[1]") #    缺勤对象
        label2 = self.getElement.get_element("xpath", "//*[@id='app']/div/div/div[2]/article/form/div[4]/div/label[2]")
        label1.click()
        label2.click()

        actbegintime = self.driver.find_element_by_xpath("//input[@placeholder='设置提醒时间']")
        time.sleep(1)
        actbegintimeStr = timeN(1)
        actbegintime.send_keys(str(actbegintimeStr))

        promisepeople = self.getElement.get_element("xpath","//*[@id='app']/div/div/div[2]/article/form/div[3]/div/div")
        promisepeople.click()
        promisesendpeople = self.getElement.get_element("xpath","//div[@role='treeitem']/div/label").click()
        time.sleep(2)
        self.getElement.get_element("xpath","//button[@class='el-dialog__headerbtn']").click()
        time.sleep(1)
        self.getElement.get_element("xpath","//button[2]").click()
        time.sleep(1)
        self.logger.info("必达发布成功！")
        time.sleep(1)
    def clickannou(self):
        try:
            announcehref = self.getElement.get_element("xpath", "//*[@id='app']/div/nav/div/div[2]/ul/li[5]")
            time.sleep(2)
            announcehref.click()
            time.sleep(2)
            self.asserttitle("公告 | TeamKit")
        except:
            self.logger.info("点击公告失败")

    def test_006_teamannou(self):
        self.clickannou()

        #管理员创建公告
    def test_006_001_createamnou(self):

        self.getElement.get_element("xpath","//*[@id='app']/div/div/div/section[1]/header/div/i[1]").click()
        announcetitleInput = self.getElement.get_element("xpath","//input[@placeholder='输入公告标题（20字符以内）']")
        announcetitleInput.send_keys("公告标题")
        announceInput = self.getElement.get_element("xpath","//textarea[@placeholder='输入公告内容']")
        time.sleep(2)
        announceInput.send_keys("公告内容")
        announcebutton = self.getElement.get_element("xpath","//*[@id='app']/div/div/div/article/form/div[4]/div/button[2]")
        announcebutton.click()

        self.logger.info("创建公告成功！")
        time.sleep(2)
    def test_006_02_list(self):
        # self.clickannou()
        #验证测试公告列表及内容
        announcelist = self.getElement.get_element("xpaths","//*[@id='app']/div/div/div/section/div/article/ul/li") #列表数据
        time.sleep(10)
        announcelist[1].click()
        # anbtn1 = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/div[2]/button[1]')
        # time.sleep(2)
        # anbtn2 = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/div[2]/button[1]')
        # time.sleep(2)
        # anbtn1.click()#取消置顶
        # anbtn2.click()#删除


    def clickculgref(self):
        try:
            culturehref = self.getElement.get_element("xpath", "//*[@id='app']/div/nav/div/div[2]/ul/li[6]")
            time.sleep(2)
            culturehref.click()
            self.asserttitle("发现 | TeamKit")
        except:

            self.logger.info("点击发现失败")

    def test_007_001_createcul(self):
        self.clickculgref()
        #发布发现
        btn = self.getElement.get_element("xpath","//*[@id='app']/div/div/div/section[2]/header/div/i[1]")
        time.sleep(2)
        btn.click()
        cultuletitleInput = self.getElement.get_element("xpath", "//input[@placeholder='输入活动标题（20字符以内）']")
        cultuletitleInput.send_keys("发现标题")
        cultuleInput = self.getElement.get_element("xpath","//textarea[@placeholder='输入发现内容']")
        cultuleInput.send_keys("发现内容")
        self.getElement.get_element('xpath',"//*[@id='app']/div/div/div/article/form/div[5]/div/button[2]").click()
        self.logger.info("发布发现成功！")
        time.sleep(1)

    def test_007_002_createcul(self):
        self.clickculgref()
        #发布外链发现文章
        btn = self.getElement.get_element("xpath","//*[@id='app']/div/div/div/section[2]/header/div/i[1]")
        time.sleep(10)
        btn.click()
        btnart = self.getElement.get_element("xpath","//*[@id='app']/div/div/div/article/nav/button[2]")
        time.sleep(2)
        btnart.click() #点击外链
        culhrefinput = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/div/div/input') #//input/[@placeholder='输入文章链接']"
        culhrefinput.send_keys("https://badlands.meixinglobal.com/informationShare/7421129?product_type=0&introduce_code=5180454&source=itrade_ios")
        btn = self.getElement.get_element("xpath", "//*[@id='app']/div/div/div/article/div/div/button")
        time.sleep(2)
        btn.click()
        time.sleep(10)
        btn = self.getElement.get_element("xpath", '//*[@id="app"]/div/div/div/article/div/div[3]/button[2]')
        time.sleep(10)
        btn.click()
        self.logger.info("发布外链文章成功")

    def click_usermer(self):
        try:
            clickmember = self.getElement.get_element("xpath", "//i[@class='mico-member']").click()
            self.logger.info("点击编辑用户信息")
            self.asserttitle("个人信息 | TeamKit")
        except:
            try:
                self.clickteam()
                clickmember
            except:
                self.logger.info("点击编辑用户信息失败")
    def test_008_usermer(self):
        self.click_usermer()
        btn = self.getElement.get_element("xpath","//section[@id='edit']/article/button[1]")
        time.sleep(6)
        btn.click()
        inputName = self.getElement.get_element("xpath","//input[@placeholder='请输入姓名']")
        inputName.send_keys("111")
        inputEnglishName = self.getElement.get_element("xpath", "//input[@placeholder='请输入英文名']")
        inputEnglishName.send_keys("ABB")
        inputWXName = self.getElement.get_element("xpath", "//input[@placeholder='请输入微信号']")
        inputWXName.send_keys("ABB")
        inputFacebookName = self.getElement.get_element("xpath", "//input[@placeholder='请输入Facebook']")
        inputFacebookName.send_keys("FC")
        time.sleep(2)
       # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 底部
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        btn = self.getElement.get_element("xpath", "//section[@id='edit']/article/button[2]")
        self.logger.info("btn-------->" + btn)
        btn.click()
        time.sleep(2)
        self.logger.info("编辑个人信息成功！")

    def clickbord(self):
        try:
            href = self.getElement.get_element("xpath","//*[@id='app']/div/nav/div/div[1]")
            href.click()
            self.logger.info("点击数据看板成功，当前用户在数据看板界面")
            self.asserttitle("客户动态 | TeamKit")
        except:
            self.logger.info("点击编辑数据看板失败，该用户没有权限")

    def screenshot(self):
        case_name = self._testMethodName
        file_path = os.path.join(os.getcwd() + "/report/" + case_name + "approval.png")

        filename = str(datetime.datetime.now())
        self.driver.save_screenshot(file_path + filename)
        # self.driver.save_screenshot("/Users/huangwenjiao/TestingScript/" + filename)
    #测试数据看板,点击后截图
    def test_009_board(self):
        self.screenshot()
        #点击按成员汇总
        self.getElement.get_element("xpath","//*[@id='board']/div[1]/a[2]")

    #封装点击产品中心
    def clickproductcenter(self):
        try:
            href = self.getElement.get_element("xpath",'//*[@id="app"]/div/nav/div/div[3]/div/span') #点击产品中心
            time.sleep(2)
            href.click()
        except:
            self.logger.info("非顶级管理员，没有产品管理权限")
    #封装点击产品管理
    def clickproductmange(self):
        self.getElement.get_element("xpath","//*[@id='app']/div/nav/div/div[3]/ul/li[1]/a").click() #点击产品管理
        time.sleep(2)
    #封装点击上传产品
    def clickuploadproduct(self):
        probtn = self.getElement.get_element("xpath","//*[@id='product']/section/header/nav/section[2]/button")
        time.sleep(2)
        probtn.click()#点击上传产品

    #上传基金类产品
    #不同类型的按钮
    #//*[@id="product"]/div[1]/div/div[2]/ul/li[2]  基金类
    def clickintodetail(self,typexpath):
        # self.clickproductcenter()
        self.clickproductmange()
        self.clickuploadproduct() # 点击上传产品
        #选择产品类型按钮
        protypebutton = self.getElement.get_element("xpath",typexpath)
        protypebutton.click()
        #点击进入录入产品详情界面
        editbtn = self.getElement.get_element("xpath",'//*[@id="product"]/div[1]/div/div[2]/section/button[2]')
        editbtn.click()

    #点击提交并发布按钮
    def clickpublishproduct(self):
        btns = self.getElement.get_element("xpaths",'//*[@id="app"]/div/div/div/article/nav/aside/button')
        btns[1].click() #发布
        time.sleep(2)
    #发布房产类/保险类/移民类必填项提交脚本一致，故封装统一
    def inputpublishproduct(self,path,input11,input22):
        path = path
        self.clickintodetail(path)
        # self.clickintopublish()
        input1 = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/section[1]/article/div/form/div[2]/div[1]/div/div/input')
        input2 = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/section[1]/article/div/form/div[2]/div[2]/div/div/input')
        # inputs2 = self.getElement.get_element("xpath", "//input[@placeholder='请输入']")
        input1.send_keys(input11)
        time.sleep(2)
        input2.send_keys(input22)
        time.sleep(2)
        self.clickpublishproduct()
    #
    def test_200_product(self):
        self.clickproductcenter()
    def test_200_001_createproduct(self):
        path = '//*[@id="product"]/div[1]/div/div[2]/ul/li[2]'
        self.clickintodetail(path)
        time.sleep(3)
        btn = self.getElement.get_element("xpath", "//*[@id='app']/div/div/div/article/div/section[1]/article/div/form/div[2]/div[1]/div/div[1]/div")
        time.sleep(3)
        btn.click()
        time.sleep(3)
        #基金产品类型
        buttons = self.getElement.get_element("xpath",'/html/body/div[2]/div[1]/div[1]/ul/li[4]/span')
        time.sleep(8)
        buttons.click()
        input1 = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/section[1]/article/div/form/div[3]/div[1]/div/div/input')
        input2 = self.getElement.get_element("xpath",'//*[@id="app"]/div/div/div/article/div/section[1]/article/div/form/div[4]/div[1]/div/div/input')
        # inputs2 = self.getElement.get_element("xpath", "//input[@placeholder='请输入']")
        input1.send_keys("Teamkit-基金类产品")
        time.sleep(2)
        input2.send_keys("Teamkit资管方")
        time.sleep(2)
        self.clickpublishproduct()
        self.logger.info("发布基金类产品成功")




    def test_200_002_createproduct(self):
        path = '//*[@id="product"]/div[1]/div/div[2]/ul/li[3]'
        self.inputpublishproduct(path,"Teamkit-房产类产品","项目")
        self.logger.info("发布房产类产品成功")
    def test_200_003_createproduct(self):
        path = '//*[@id="product"]/div[1]/div/div[2]/ul/li[4]'
        self.inputpublishproduct(path,"Teamkit-保险类产品","Teamkit")
        self.logger.info("发布保险类产品成功")
    def test_200_004_createproduct(self):
        path = '//*[@id="product"]/div[1]/div/div[2]/ul/li[5]'
        self.inputpublishproduct(path,"Teamkit-移民类产品","Teamkit")
        self.logger.info("发布移民类产品成功")
    #退出登录
    def test_300_01_exitlogin(self):
        btn = self.getElement.get_element("xpath",'//*[@id="app"]/div/header/span[2]/div/img[1]')
        time.sleep(3)
        btn.click()
        exitloginbtn = self.getElement.get_element("xpath",'//*[@id="el-popover-1019"]/ul/div[2]/li[2]')
        time.sleep(2)
        exitloginbtn.click()
        self.getElement.get_element("xpath",'/html/body/div[3]/div/div[3]/button[2]').click()

#理财计算器的测试用例
    #封装点击工作平台
    def clicktoolsection(self):
        toolsectionbtn = self.getElement.get_element("xpath",'//*[@id="app"]/div/nav/div/div[4]/div/span')
        toolsectionbtn.click()

    #封装点击 理财报表
    def clickcalcul(self):
        btn = self.getElement.get_element("xpath",'//*[@id="app"]/div/nav/div/div[4]/ul/li/a')
        btn.click()

    #点击新建项目
    #进行新建项目,输入项目名称为 项目，点击保存
    def createitem(self):
        createitembtn = self.getElement.get_element("xpath",'//*[@id="calculator"]/section/div/div/section/button/span')
        createitembtn.click()
        ietminput = self.getElement.get_element("xpath",'//textarea[@placeholder="请输入项目名称"]')
        ietminput.send_keys("项目")
        itemsavebtn = self.getElement.get_element("xpath",'/html/body/div[3]/div/div[3]/button[2]/span')
        itemsavebtn.click()

    #获取项目列表的数据
    #返回表单内的td 的数据
    def getitemslist(self):
        lists = self.getElement.get_element("xpaths",'//*[@id="calculator"]/section/div/div/section/div[1]/div/div[3]/table/tbody/tr')
        return lists

    #点击列表第一个详情按钮
    def clickfirstbtn(self):
        btn = self.getElement.get_element("xpath",'//*[@id="calculator"]/section/div/div/section/div[1]/div/div[3]/table/tbody/tr[1]/td[5]/div/button[1]')
        btn.click()

    #获取详情按钮，第i个，从1开始?
    def getdetailbtn(self,i):

        btn = self.getElement.get_element("xpaths",'//*[@id="calculator"]/section/div/div/section/div[1]/div/div[3]/table/tbody/tr[i]/td[5]/div/button[1]')



if __name__ == '__main__':
    reportHtml = "webmanger"+ datetime.datetime.now().strftime("%Y-%m-%d")+".html"
    # 文件名字
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "report")
    # file_path = log_dir + "/" + reportHtml
    file_path = os.path.join("/Users/huangwenjiao/TestingScript/seleniumTestcase/"+reportHtml)
    print(file_path)
    print(file_path)
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_001_login'))
    suite.addTest(FirstCase('test_002_act'))
    suite.addTest(FirstCase('test_002_act_create_001'))
    suite.addTest(FirstCase('test_002_act_create_002'))
    suite.addTest(FirstCase('test_002_act_create_003'))
    suite.addTest(FirstCase('test_002_act_create_004'))
    suite.addTest(FirstCase('test_002_act_edit_006'))
    suite.addTest(FirstCase('test_002_act_apply_005'))
    suite.addTest(FirstCase('test_003_appro_list'))
    suite.addTest(FirstCase('test_004_01_createdayreport'))
    suite.addTest(FirstCase('test_004_02_createweekreport'))
    suite.addTest(FirstCase('test_004_03_createmonthreport'))
    #
    suite.addTest(FirstCase('test_004_05_editreport'))
    suite.addTest(FirstCase('test_004_06_seereport'))
    suite.addTest(FirstCase('test_004_07_deletecrereport'))
    suite.addTest(FirstCase('test_004_08_deletemanareport'))
    suite.addTest(FirstCase('test_004_09_approreport'))
    suite.addTest(FirstCase('test_005_01_createpromise'))
    suite.addTest(FirstCase('test_006_teamannou'))
    suite.addTest(FirstCase('test_006_001_createamnou'))

    suite.addTest(FirstCase('test_006_02_list'))
    suite.addTest(FirstCase('test_007_001_createcul'))
    suite.addTest(FirstCase('test_007_002_createcul'))
    suite.addTest(FirstCase('test_008_usermer'))
    suite.addTest(FirstCase('test_009_board'))
    suite.addTest(FirstCase('test_200_product'))
    suite.addTest(FirstCase('test_200_001_createproduct'))
    suite.addTest(FirstCase('test_200_002_createproduct'))
    suite.addTest(FirstCase('test_200_003_createproduct'))
    suite.addTest(FirstCase('test_200_004_createproduct'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title=" Teamkit web 测试报告",description=u"1111",verbosity=2)

    runner.run(suite)