import time
import random
import requests
from log.user_log import UserLog
class Teamkitlogintoken(object):

    def __init__(self):
        self.url = "https://dnapp.bitkinetic.com/api/v5/login/mplogin"
        self.body = {
            "zoneNum": "86",
            "phone": "15088132074",
            "password": "123456"
        }

        self.logger = UserLog().get_log()

        print("初始化")


    # 获取指定长度的随机字符串
    def __getRandomStr__(self,len):

        # 获取len位的随机字符串
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(len):
            sa.append(random.choice(seed))

        randomStr = ''.join(sa)

        return randomStr

    # # 返回json格式,传入字典格式
    # def __returnJson__(keys, values):
    #
    #     mJson = dict(zip(keys, values))
    #
    #     mJson = json.dump(mJson)
    #
    #     return mJson

    # 传入 手机号、区号、密码，返回可正常登录形式
    # def userinfo(phone, zoneNum, password):
    #
    #     keys = ["phone", "zoneNum", "password"]
    #
    #     value = [phone, zoneNum, password]
    #
    #     data = dict(zip(keys, value))
    #
    #     data = json.dump(data)
    #
    #     return data

    # 获取加密之后的hash串（int）
    def __calcSign__(self,salt, hash, time):
        for i in salt:
            hash = ((hash << 5) & 0x7fffffff) + int(ord(i)) + hash
        return (hash & int(time))

    # 获取请求头
    # 登录接口需传入的参数
    def __getHttpHeader__(self):

        # 获取当前时间，为秒单位
        t = str(int(time.time()))

        # 获取随机字符串
        r = self.__getRandomStr__(32)

        # 定义当前版本号
        version = 2019

        sign = str(self.__calcSign__(r, version, t))

        header = {'r': r, 't': t, 'sign': sign, 'd-version': str(version)}

        return header

        # 执行登录接口调用
    def login(self):

        url = self.url

        body = self.body

        header = self.__getHttpHeader__()

        response = requests.post(url, data=body, headers=header).json()
        print(response)
        if response["ret"] == 0:
            self.logger.info("登录账号信息：" + str(body) + "登录成功")
            return response
        else:
            print(response["msg"])
            self.logger.info("login--->")
            self.logger.info("登录账号信息：" + str(body) )
            self.logger.info(response)




    def getMerloginHeader(self):

        res = self.login()
        dtToken = res['data']['d-tk']  #获取token
        iTeams = res['data']['user_info']['team']  #获取iTeam 内的字段


        t = str(int(time.time()))

        # 获取随机字符串
        r = self.__getRandomStr__(32)

        # 定义当前版本号
        version = 2019

        sign = str(self.__calcSign__(r, version, t))

        app = "3001" #3001为Teamkit

        dnapp = "100001"


        if len(iTeams) > 1 :
            for iTeam in iTeams:
                # print(iTeam)
                if iTeam["iRole"] ==  4  or iTeam["iRole"] == 1 or iTeam["iRole"] == 2:
                    iManagerTeamId = iTeam["iTeamId"]
                    iManageName = iTeam["sTeamName"]
                    iManegeTeamrole = iTeam["iRole"]
                    header = {'app': app, "dnapp": dnapp, 'r': r, 't': t, 'sign': sign, 'd-version': str(version),
                              'd-tk': dtToken, 'teamrole': str(iManegeTeamrole), 'iTeamId': str(iManagerTeamId)}  # 成员身份的请求头

                elif iTeam["iRole"]  == 3:
                    iMermeTeamId = iTeam["iTeamId"]
                    iMerTeamName = iTeam["sTeamName"]
                    iMerTeamrole = iTeam["iRole"]
                    Managerheader = {'app': app, "dnapp": dnapp, 'r': r, 't': t, 'sign': sign, 'd-version': str(version),
                                     'd-tk': dtToken, 'teamrole': str(iMerTeamrole),
                                     'iTeamId': str(iMermeTeamId)}  # 管理员参数的请求头

        else:
            print("未加入团队")


        # header = {'app': app,"dnapp":dnapp,'r': r, 't': t, 'sign': sign, 'd-version': str(version),'d-tk':dtToken,'teamrole':str(teamrole),'iTeamId':iTeamId}


        return header,Managerheader
#
# tktoken = Teamkitlogintoken()
# tktoken.url = "https://dnapp.bitkinetic.com/api/v5/login/mplogin"
# tktoken.body = {
#     "zoneNum": "86",
#     "phone": "15088132074",
#     "password": "123456"
# }
# tks = tktoken.getMerloginHeader()
# mertoken = tks[0]
# mantoken = tks[1]
# print("9998888777")
# print(mertoken)
#
