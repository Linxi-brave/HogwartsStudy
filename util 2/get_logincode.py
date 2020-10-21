import time
import urllib
import os
import zxing
import requests
from util.get_tklogintoken import Teamkitlogintoken
class qrcode(object):
    def __init__(self,driver):
        self.driver = driver
        # self.url = "https://dnapp.bitkinetic.com/api/v5/user/qrcodelogin"

    def get_qrcode(self):
        self.img_url = self.driver.find_element_by_xpath("// *[ @ alt = '二维码']")
        time.sleep(2)
        print(self.img_url)
        self.relimg_ulr = self.img_url.get_attribute("src")
        print(self.relimg_ulr)
        # 保存图片到指定路径
        if self.relimg_ulr != None:
            filename = '/qcode.jpg'
            # 保存图片数据
            data = urllib.request.urlopen(self.relimg_ulr).read()
            filepath = os.path.join(os.getcwd() ,'img')
            print("112223444")
            print(filepath)
            f = open(filepath + filename, 'wb')
            f.write(data)
            f.close()

        reader = zxing.BarCodeReader()
        path = os.path.join(os.getcwd() ,'img')
        filepath = path + "/qcode.jpg"
        print(filepath)
        barcode = reader.decode(filepath)
        codelist = str(barcode).split("'")
        return codelist
    #得到参数
    def getcode(self,codelist):
        print("codelist-->")
        print(codelist)
        for value in codelist:
            if value.find("pcQrCodeLogin://") == 0:
                codeStr = value
                code = codeStr[16:]
                return code
                break
    #扫码登录

    # type = status ,扫描尝试登录 ； type =login，进行登录
    def qrcodelogin(self,query, type,url,header):
        urlmemberinfo =  url

        body = {
            "query": query,
            "type": type
        }
        print(header)
        print(body)
        print(query)
        response = requests.post(urlmemberinfo, data=body, headers=header).json()


    def toqrcodelogin(self,url,header):
        print("toqrcodelogin")
        codelist = self.get_qrcode()
        query = self.getcode(codelist)
        self.qrcodelogin(query,"status",url,header)
        self.qrcodelogin(query,"login",url,header)
