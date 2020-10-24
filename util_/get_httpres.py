import requests
from log.user_log import UserLog
from util.send_email import sendmail
from util.base import BaseAction
class httprequest(object):
    def __init__(self,host):
        log = UserLog()
        self.logger = log.get_log()
        self.host = host
        self.smail = sendmail()
        self.errorlog = BaseAction()
        # self.testurl = testurl
        # host = "host"
        # testurl = "testurl"
    def testapi(self,testurl, body, header):
        # header = getMerloginHeader()
        url = self.host + testurl
        res = requests.post(url, data=body, headers=header).json()
        self.logger.info("请求：" + str(testurl) + "请求参数:" + str(body) + "请求结果:" + str(res))

        if requests.status_codes == 500:
            self.errorlog.errorloginfo()
            return False
        else:

            return True
    #调用url函数
    def testapimethod(self,testurl,body,header,method):
        url = self.host + testurl
        try :
            if method == "post":
                res = requests.post(url, data=body,headers =header).json()
            elif method == "get":
                res = requests.get(url, data = body , header = header).json()
            elif method == "put":
                res =requests.put(url,data = body,headers = header).json()
        except:
            self.errorlog.errorloginfo()
        if requests.status_codes == 200:
            return res
        else:
            return False



    def getapires(self,testurl,body,header):
        # header = getMerloginHeader()
        url = self.host + testurl
        res = requests.post(url,data=body,headers=header).json()
        self.logger.info("请求：" + str(testurl) + "请求参数:" + str(body) + "请求结果:" + str(res))
        if requests.status_codes == 500:
            self.errorlog.errorloginfo()
            return False
        else:
            return res