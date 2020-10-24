#coding=utf-8
import sys
import os
import json
import requests
base_path = os.getcwd()
sys.path.append(base_path)
from util.handle_json2 import read_json,write_value
from util.get_tklogintoken import Teamkitlogintoken
from util.handle_init import HandleInit
def get_header(filename = None):
    if filename == None :
        data = read_json("/config/header.json")
    else:
        data = read_json(filename)
    return data

def write_hearder(data,hearder_key,jsonfile=None):
    if jsonfile == None:
        data1 = read_json("/config/header.json")
    data1 = read_json(jsonfile)
    data1[hearder_key] = data
    write_value(data1)

def get_mlurl():
    hi = HandleInit()
    host = hi.get_value("server","host")
    mlurl = host + '/api/v5/login/mplogin'
    print('mlurl---->',mlurl)
    return mlurl

def get_jy_mlurl():
    '''
    获取简盈登录的URL ，动态获取
    '''
    hi = HandleInit()
    host = hi.get_value("server","jyhost")
    url = hi.get_value("server","jyloginurl")
    jymlurl = host + url
    return jymlurl

def get_jy_mlbody():
    '''
    获取简盈登录的body值，动态获取
    '''
    hi = HandleInit()
    jyphone = hi.get_value("server","jyphone")
    jypassword = hi.get_value("server","jypassword")
    jyzomeNum = hi.get_value("server","jyarea_code")
    keys = ['phone','password','area_code']
    value = [jyphone,jypassword,jyzomeNum]
    data = dict(zip(keys,value))
    data = json.dumps(data)
    data = json.loads(data)
    # print(data)
    return data

def get_mlbody():
    hi = HandleInit()
    phone = hi.get_value("server","phone")
    pw = hi.get_value("server",'pw')
    zoneNum = hi.get_value("server","zoneNum")
    keys = ["phone", "zoneNum", "password"]
    value = [phone,int(zoneNum),pw]
    data = dict(zip(keys,value))
    data = json.dumps(data)
    data = json.loads(data)
    print(data)
    return data


def get_teamkimertoken():
    url = get_mlurl()
    body = get_mlbody()
    tktoken = Teamkitlogintoken()
    if url == None:
        tktoken.url = "https://dnapp.bitkinetic.com/api/v5/login/mplogin"
    else:
        tktoken.url = url
    if body == None:

        tktoken.body = {
            "zoneNum": "86",
            "phone": "15088132074",
            "password": "123456"
        }
    else:
        tktoken.body = body

    tks = tktoken.getMerloginHeader()
    mertoken = tks[0]
    mantoken = tks[1]
    print("-------")
    print(mertoken)
    print(type(mertoken))
    return mertoken,mantoken


def get_jy_header():
    '''
    获取到简盈登录的token ，以拿到请求头，可进行登录态的请求
    '''
    hi = HandleInit()
    jyphone = hi.get_value("server","jyphone")
    jypassword = hi.get_value("server","jypassword")
    jyzomeNum = hi.get_value("server","jyarea_code")

    body = {
        "phone":jyphone,
        "password":jypassword,
        "area_code":86 }
    header = {"Content-Type":"application/json","app":"jy","version":"1.0.0"}
    # body = {"phone":"13682575156","area_code":86,"password":"111111"}
    # print(type(body))
    body = json.dumps(body)


    url = get_jy_mlurl()

    res = requests.post(url,data = body,headers = header).json()
    if res["code"] == 200:
        token = res["data"]["token"]
        header = {"Content-Type": "application/json","app":"jy","version":"1.0.0","Authorization":token}

        return header
    else :
        print(res)
        print(type(res))




def writer_tk_merberhearder():

    mertoken = get_teamkimertoken()[0]

    if mertoken != None:
        # mertoken = json.dumps(str(mertoken))
        # # json.loads(mertoken)
        # print(type(mertoken))
        # write_hearder(mertoken,"/config/tk_merberhearder.json")
        return mertoken
    else:
        return None


def writer_tk_mangerhearder():

    mangertoken = get_teamkimertoken()[1]
    if mangertoken != None:
        # write_hearder(mangertoken,"/config/tk_mangerhearder.json")
        return mangertoken
    else:
        return None

#
# print(sys.path.append(base_path))
# # get_teamkimertoken()
# writer_tk_merberhearder()
# get_jy_header()