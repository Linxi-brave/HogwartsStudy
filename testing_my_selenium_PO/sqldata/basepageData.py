import pytest

from util.handle_mysql import HandleSql
from util.handle_yaml import HandleYaml
import os
import time,datetime
class BasepageData():

    def __init__(self):
        self.handleyaml = HandleYaml()
        sqlaccount = self.handleyaml.getSqlaccountData()
        # self.handlesql = HandleSql()
        self.handlesql = HandleSql(sqlaccount[0],sqlaccount[1],
                                   sqlaccount[2],sqlaccount[3])

    def sql_yhgllistdata(self):
        '''获取数据库用户管理列表的数据'''
        # sql = 'SELECT tu.iUserId,tu.sName,tu.sPhone,tu.dtRegtime FROM dbuser.tbuser as tu LEFT JOIN dbvip.tbuservip as tuv ON tu.iUSerId = tuv.iUSerId WHERE tu.iAppId = 100001 ORDER BY tu.iUSerId DESC LIMIT 10'
        sql = 'SELECT tu.iUserId,tu.sName,tu.sPhone,tu.dtRegtime FROM dbuser.tbuser AS tu  WHERE tu.iAppId = 100001  ORDER BY tu.iUserId DESC LIMIT 10 '
        data = self.handlesql.sql_alldata(sql)

        return data



if __name__ == '__main__':
    baseData = BasepageData()

    print(baseData.sql_yhgllistdata())

    # print(baseData.testdatetime())
