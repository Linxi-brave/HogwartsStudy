# coding=utf-8
import yagmail
import os
import time
# import mysql
# from commons.mysql import *
class sendmail(object):
    #封装发送测试报告邮箱
    def sendTestReportEmail(self):
        sendmail.testEmail()
        sendmail.errorEmail()

    #如果有报错500，就发送邮件
    def errorEmail(self):
        fileName = '/Users/huangwenjiao/error/' + "log" + time.strftime('%Y-%m-%d', time.gmtime()) + '.txt'
        if sendmail.checkFile(fileName):
            sendmail.sendmail('hwj@insucrm.com', '测试失败', "",fileName)

    def testEmail(self):
        fileName = '/Users/huangwenjiao/' + "log" + time.strftime('%Y-%m-%d', time.gmtime()) + '.txt'
        print(fileName)
        if sendmail.checkFile(fileName):
            print(fileName)
            sendmail.sendmail("hwj@insucrm.com",'今天测试','测试')

    #如果今日日志不存在，则创建文件
    def checkFile(file):
        if not os.path.isfile(file):
            return False
        else:
            return True
        # print("文件存在！")

    # 发送正文，不带附件
    def sendmail(users,subjecttitle,contents):
        yag = yagmail.SMTP(user="15088132074@163.com", password="123456Wj@", host='smtp.163.com')

        # 发送邮件
        yag.send(users, subjecttitle, contents)
        # #发送带附件的邮件
    def sendmailFile(self, users,subjecttitle,contents,file):
        yag = yagmail.SMTP(user="15088132074@163.com", password="123456Wj@", host='smtp.163.com')

        # 发送邮件
        yag.send(users, subjecttitle, contents,file)
        # yag.send('15088132074@163.com', '发送附件', contents, ["d://testresult.html"])






        # 成功的例子
        # yag = yagmail.SMTP(user="15088132074@163.com", password="15088132074wj", host='smtp.163.com')
        #
        #
        # # 邮箱正文
        # contents = ['This is the body, and here is just text http://somedomain/image.png',
        #             'You can find an audio file attached.', '/local/path/song.mp3']
        #
        # # 发送邮件
        # yag.send('15088132074@163.com', 'subject', contents)
        #
        # #给多个用户发送邮件#
        # # 发送邮件
        # yag.send(['15088132074@163.com','730162062@qq.com'], 'subject', contents)
        # #发送带附件的邮件
        #yag.send('15088132074@163.com', '发送带附件的邮件', contents, ["d://testresult.html"])
