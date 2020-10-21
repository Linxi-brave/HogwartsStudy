#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from util.handle_excel import excel_data
from jsonpath_rw import parse
import json

def split_data(data):
    '''
    拆分单元格数据
    '''
    #imooc_005>data:banner:id
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data

def depend_data_m(data,filepath = None):  #获取对应的接口请求返回值
    '''
    获取依赖结果集
    '''
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id,filepath)
    data = excel_data.get_cell_value(row_number,14,filepath)
    return data


def get_depend_data(res_data,key):  #获取json 中对应的某个值，如 data:banner:id 的值
    '''
    获取依赖字段
    '''
    res_data = json.loads(res_data)

    json_exe = parse(key)
    madle = json_exe.find(res_data)
    # res_data = json.dumps(res_data)
    return [math.value for math in madle][0]

def get_data(data):
    '''
    获取依赖数据
    '''
    res_data = depend_data_m(data)   #获取对应的接口请求返回值
    rule_data = split_data(data)[1]  #获取json对应的关键字，如：data:banner:id
    print(rule_data)
    res_data = json.dumps(res_data)
    return get_depend_data(res_data,rule_data)

#data ：判断参数，例子：keys > code;data.user_info.iUserId
#res：接口返回值
#expres：预期结果的返回值
#返回为False代表失败
def get_keys_assert(data,res,expres):
    data1 = split_data(data)[1]
    datas = data1.split(";")
    for i in range(0,len(datas)):
        keys = data[i]
        print("keys--->",keys)
        json_exe = parse(keys)
        madle = json_exe.find(res)
        print(madle)
        expresmadle = json_exe.find(expres)
        resvalue = [math.value for math in madle][0]
        expresvalue = [math.value for math in expresmadle][0]
        if resvalue == expresvalue:
            return True
        else:
            return False






if __name__ == "__main__":

    # res = {"code": 200, "msg": "success", "data": {"page": {"currPage": 1, "pageNum": 3, "rowsCount": 25}, "reList": [{"aov": 1, "checkAudition": 2, "cid": 30, "discount": 2, "discountPrice": 0, "free": 2, "havBuy": 2, "img": "https://icon-img.bitkinetic.com/dn/course/img/E04A1E1B-1AE5-4930-A1B9-35EC293F1758", "listImg": "https://icon-img.bitkinetic.com/dn/course/img/0E50EEAE-1337-4F16-96B5-B9909B8F3B84", "originalPrice": 0.01, "period": 1, "readCnt": 1, "specPrice": 0, "specials": 2, "title": "uUGG"}, {"aov": 2, "checkAudition": 2, "cid": 29, "discount": 2, "discountPrice": 0, "free": 2, "havBuy": 1, "img": "https://icon-img.bitkinetic.com/dn/course/img/A34CD950-8E39-4539-9E9E-6B4EB988B747", "listImg": "https://icon-img.bitkinetic.com/dn/course/img/3C87A97E-04B8-4F53-8715-A70C4382ADF0", "originalPrice": 0.01, "period": 0, "readCnt": 11, "specPrice": 0, "specials": 2, "title": "\u6d4b\u8bd5\u6d4b\u8bd5"}, {"aov": 2, "checkAudition": 1, "cid": 27, "discount": 2, "discountPrice": 0, "free": 2, "havBuy": 1, "img": "https://icon-img.bitkinetic.com/dn/course/img/0698819D-37E7-46D6-B20C-4A0B0F743AAA", "listImg": "https://icon-img.bitkinetic.com/dn/course/img/6B1FCAAA-754B-484D-9F70-787A3520C8C0", "originalPrice": 80, "period": 100, "readCnt": 355, "specPrice": 0, "specials": 2, "title": "\u91d1\u878d\u5feb\u8baf\uff1a\u7ebd\u7ea6\u5b9e\u65f6\u8fde\u7ebf\u7cfb\u7edf\u97f3\u9891"}]}}
    # res = json.dumps(res)
    # data = 'testcase_003>data.reList.[0].cid'
    # data = get_depend_data(res,data)
    # print(data)

    # res = {"ret": 100005, "code": 100005, "msg": "\u62b1\u6b49\uff0c\u60a8\u7684\u767b\u5f55\u6001\u5df2\u5931\u6548,\u8bf7\u91cd\u65b0\u767b\u5f55", "data": []}
    #
    # expres = {"code":200,"data.user_info.iUserId":23}
    #
    # data = "keys>code"
    #
    # get_keys_assert(data,res,expres)
    data1 = {"page":"1","num":"12","cid":8}
    filepath = '/case/jyapitest.xlsx'
    res_data = depend_data_m("testcase_003>data.reList.[0].cid",filepath= filepath)
    rule_data = split_data("testcase_003>data.reList.[0].cid")[1]
    data = get_depend_data(res_data,rule_data)
    depen_key = 'cid'
    data1[depen_key] = data
    print(rule_data)
    print(res_data)
    print(data)
    print(data1)




    # get_data("testcase_006>data[0].iAnnounceId")
    #
    # print(depend_data("testcase_006>data[0].iAnnounceId"))
    # res_data = {
    #      "ret": 0,
    #      "code": 200,
    #      "msg": "ok",
    #      "data": [{
    #       "iAnnounceId": 690,
    #       "iBuilderId": 7,
    #       "sRealName": "黄文娇",
    #       "sAvatar": "https:\/\/app-img.bitkinetic.com\/tk\/User\/Avatar\/7\/2020\/04\/R1587006513dn5e97cc31b0daf",
    #       "iReadNum": 4,
    #       "iUnreadNum": 10,
    #       "iRead": 0,
    #       "iMemberNum": 14,
    #       "sTeamName": "保城精英团队",
    #       "sTitle": "公告标题",
    #       "sContent": "公告内容",
    #       "isTopping": 1,
    #       "isManager": 1,
    #       "dtReleaseTime": 1586503041,
    #       "currentPage": "1",
    #       "nextPage": "2"
    #      }]}
    #
    # res_data = json.dumps(res_data)
    #
    # print(get_depend_data(res_data,'data[0].iAnnounceId'))
    #
    #
    # # get_data('testcase_006>data[0].iAnnounceId')
    # # get_data('testcase_006>data[0].iAnnounceId')
    # # data = {
    # #     "a":"a1",
    # #     "b":"b1",
    # #     "c":[
    # #         {
    #             "d":"d1"
    #         },
    #         {
    #             "d":"d2"
    #         }
    #     ]
    # }
    #
    # data = json.dumps(data)
    # key = 'c.[1].d'
    # print(get_depend_data(data,key))

    # get_data("testcase_006>data[0].iAnnounceId")



    # print(get_data('testcase_006>data[0].iAnnounceId'))

    # print(depend_data)
    #
    # depend_data = get_data(is_depend)
    # data1[depend_key] = depend_data
    # print(data1)


    # depend_key = "iAnnounceId"  # iAnnounceId
    # is_depend = "testcase_006>data[0].iAnnounceId"
    # data1 = {
    #  "iAnnounceId": "690"
    # }
    # key1 = 'iAnnounceId'

# print(depend_data)
