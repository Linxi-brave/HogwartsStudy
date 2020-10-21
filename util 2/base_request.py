#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from util.handle_cookie import write_cookie
from util.handle_init import HandleInit
from log.user_log import UserLog

class BaseRequest:
    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        '''
        发送post请求
        '''
        response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        if get_cookie !=None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar =  response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res
    
    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        '''
        发出get请求
        '''
        response = requests.get(url=url,params=data,cookies=cookie,headers=header)
        if get_cookie !=None:
            cookie_value_jar = response.cookie
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])

        res = response.text
        return res
    
    def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None,app = None):
        '''
        执行方法，传递method、url、data参数
        '''
        #return get_value(url)
        # base_url = HandleInit.get_value("server","host")
        hi = HandleInit()
        log = UserLog().get_log()


        if 'http' not in url:

            if  app == "jy":
                '''
                兼容简盈APP
                '''
                base_url = hi.get_value("server","jyhost")

                url = base_url + str(url)

                jyheader = {"Content-Type": "application/json","app":"jy","version":"1.0.0"}


                if method == 'get':

                    res = self.send_get(url,data,cookie,get_cookie,header)

                    log.info("http --》url---->")
                    log.info(url)
                    log.info("http--->data---->")
                    log.info(data)
                    log.info("http--->header--->")
                    log.info(header)
                    log.info("http--->res--->")
                    log.info(res)
                else:

                    res = self.send_post(url,data,cookie,get_cookie,header)
                try:
                    res = json.loads(res)
                except:
                    print("这个结果是一个text")
                # print("--->",res)
                return res
            else  :
                base_url = hi.get_value("server","host")

                url = base_url + str(url)


                if method == 'get':
                    res = self.send_get(url,data,cookie,get_cookie,header)
                else:
                    res = self.send_post(url,data,cookie,get_cookie,header)
                try:
                    res =json.loads(res)
                except:
                    print(" 这个结果是一个text")
                    print(res)
                return res
        else:
            if method == "get":
                res = self.send_get(url,data,cookie,get_cookie,header)
            else :
                res = self.send_post(url,data,cookie,get_cookie,header)
            return res





    def run_request_js(self,method,url,data,cookie=None,get_cookie=None,hearder=None):
        if method == 'get':
            res = self.send_get(url,data,cookie,get_cookie,hearder)
        else:
            res =self.send_post(url,data,cookie  ,get_cookie,hearder)

        # resjson  = json.loads(res)
        return res

    
    
request = BaseRequest()
if __name__ == "__main__":
    # request = BaseRequest()
    # h = get_jy_header()
    #
    # data = {"page":"1","num":"12"}
    # res = request.run_main("get","/course/v1/my/list",data,header = h,app = "jy")
    # print(res)

    host = "https://api.mxcloud.work"
    request = BaseRequest()
    data = {"phone": "13602575156", "area_code": 86, "password": "111111"}
    data = json.dumps(data)
    hearders = {
        "Host": "api.mxcloud.work",
        "version": "1.0.2",
        "Authorization": "",
        "Accept": "*/*",
        "r": "87733eef710d42bb9b03542553a3840e",
        "os": "ios",
        "Accept-Language": "zh-Hans-CN;q=1, zh-Hant-HK;q=0.9, en-IN;q=0.8, ja-CN;q=0.7, en-GB;q=0.6, yue-Hant-CN;q=0.5",
        "app": "jy",
        "Accept-Encoding": "gzip, deflate, br",
        "t": "1601185851",
        "Content-Length": "58",
        "User-Agent": "jian ying gui hua/1.0.2 (iPhone; iOS 13.6; Scale/2.00)",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "sign": "203434002",
    }
    res = request.send_post("https://api.mxcloud.work/user/uc/v1/login/mp", data, header=hearders)


    res = json.loads(res)
    token = res["data"]["token"]
    print(res["data"]["token"])


    # res = request.run_main('post','/api/v5/login/mplogin',"{'username':'11111'}")
    # res = request.run_request_js('post','https://app.harvestwm.cn/api/v1/app/preregister','{"mobile":"13602575156","verifyCode":"3479","purpose":"mobilereg"}')
    # hearder = {'appversion':'2.4.1','Content-Length':'122','Accept-Language':'zh-cn','User-Agent':'JiaShiCaiFuApp/100 CFNetwork/1126 Darwin/19.5.0','Content-Type':'application/json'}
    # res2 = request.run_request_js('post','https://app.harvestwm.cn/api/v1/app/login','{"loginId":"13602575156","password":"d2a6d9f4337a0c12d0fc86bf671789e9d0ebeb6cad5f1d796adfd0ab911490f1","passwordStrong":2}',hearder = hearder)
    # # res = requests.post('https://app.harvestwm.cn/api/v1/app/login','{"loginId":"13602575156","password":"d2a6d9f4337a0c12d0fc86bf671789e9d0ebeb6cad5f1d796adfd0ab911490f1","passwordStrong":2}')
    # data = ''
    # res33= requests.get("https://app.harvestwm.cn/api/v1/app/fundrankings/performance?buyFlag=1&dataCode=&pageNo=1&sortBy=yieldFor3Month&sortOrder=D&totalPage=315",'data')
    # print(res33.text)
    # print(json.loads(res33.text)["performanceList"][0])
    # list = json.loads(res33.text)["performanceList"]
    # for i in range(0,len(list)-1):
    #     print(list[i]["fundCode"])
    #     print(list[i]["fundName"])

    # for i in range(1,3):
    #     url = 'https://app.harvestwm.cn/api/v1/app/fundrankings/performance?buyFlag=1&dataCode=&sortBy=yieldFor3Month&sortOrder=D&totalPage=315&pageNo=' + str(i)
    #     res = requests.get(url)
    #     list = json.loads(res.text)['performanceList']
    #
    #     for i in range(0,len(list) - 1):
    #         # print(list[i]["fundCode"])
    #         # print(list[i]["fundName"])
    #         fundCodelist = []
    #         # print(type(fundCodelist))
    #         funcode = list[i]["fundCode"]
    #         print(funcode)
    # #         fundCodelist = fundCodelist.append(funcode)
    # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0Tm8iOiIxNDI1NzYiLCJpYXQiOjE1OTQ3MTAxMzgsImV4cCI6MTU5NjAwNjEzOH0.RtyZptIWrwOTw0I7cOI8lORGKxlHJNeRF4c4pvRM4Gw'
    # data2 = '{"balance":10,"fundCode":"005481","tradeAcco":"900300039024","channel":"allinpay","needAddBranch":false,"capitalMode":"M","password":"6ae90f870a2a30f622a61a9a54d79b1c42ed2c5943aff873da913e456264a97e","promotionId":null,"configValue":"0","passwordStrong":2}'
    # headers = {'appversion': '2.4.1', 'Content-Length': '122', 'Accept-Language': 'zh-cn',
    #                 'User-Agent': 'JiaShiCaiFuApp/100 CFNetwork/1126 Darwin/19.5.0',
    #                 'Content-Type': 'application/json', 'token': token}
    # #
    # url1 = 'https://app.harvestwm.cn/api/v1/app/buy/fare?balance=10&businFlag=022&capitalMode=M&channel=allinpay&fundCode=005481&needAddBranch=false&tradeAcco=900300039024'
    # data1 = ''
    # res1= request.run_request_js("get",url1,data1,headers)
    #
    # url2 = 'https://app.harvestwm.cn/api/v1/app/buy'
    #
    # res2 = request.run_request_js("post",url2,data2,headers)
    # print(res1)
    # print(res2)
    # code = "EG1037"
    # host = 'https://app.harvestwm.cn'
    # testurl = host +'/api/v1/app/privateproductdetail?fundCode=' + code
    # data = {"fundCode":code}
    # print(type(data))
    #
    # res2 = request.send_get(testurl,data,header = headers)
    # print("token")
    # print(res2)


    # jsonres = res33.split("}',")[1]
    # print(jsonres)
    # print(type(res33))
    # print(json.dumps(jsonres))
    # print(type(json.loads(jsonres)))
    # print(json.loads(jsonres)['status']['message'])
    # print(json.dumps(res))
    # print(type(json.dumps(res)))
