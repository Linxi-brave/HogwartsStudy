import pymysql
pymysql.install_as_MySQLdb()

import pymysql.cursors
from util.user_log import UserLog
# # host = mysql-server.testing.svc.cluster.local , port =  3306 , user = dn ,password =  dn@2018
# conn = pymysql.connect(host = 'mysql-server.testing.svc.cluster.local' ,port = 3306 ,user = 'dn',passwd = 'dn@2018',db = "dbuser")
# cur = conn.cursor()
# cur.execute("select * from tbapp")
# for r in cur.fetchall():
#     print(r)
# conn.close()


class HandleSql(object):
    def __init__(self,host=None,port=None,user=None,passwd=None):
        if host == None:
            self.host = 'mysql-server.testing.svc.cluster.local'
        else:
            self.host = host
        if port == None:
            self.port = 3306
        else:
            self.port = port
        if user == None:
            self.user = 'dn'
        else:
            self.user = user
        if passwd == None:

            self.passwd = 'dn@2018'
        else:
            self.passwd = passwd
        self.logger = UserLog().get_log()

    def connsql(self):
        try:
            conn = pymysql.connect(
                host = self.host,port = self.port,user = self.user ,passwd = self.passwd)
            cur = conn.cursor()
            return cur,conn
        except Exception as e:
            self.logger.info(e)
            print(e)
            print("连接数据库失败")

    def closesql(self,conn,cur):
        try :
            #游标关闭
            cur.close()
            #提交事务
            conn.commit()
            #关闭连接
            conn.close()
        except Exception as e:
            self.logger.info(e)
            print(e)

    def sql_alldata(self,sql):
        '''返回查询的所有数据'''
        cur = self.connsql()[0]
        conn = self.connsql()[1]
        if cur == None:
            self.connsql()
        try:
            cur.execute(sql)
            datas = cur.fetchall()
            return datas

        except Exception as e:
            self.logger.info(e)
            print(e)
        finally:
            if cur:
                self.closesql(conn,cur)

    def sal_manydata(self,sql,n):
        '''获取几行的数据'''
        cur = self.connsql()[0]
        conn = self.connsql()[1]
        if cur == None:
            self.connsql()
        try:
            cur.execute(sql)
            datas = cur.fetchmany(n)
            return datas
        except Exception as e:
            self.logger.info(e)
            print(e)
        finally:
            if cur :
                self.closesql(conn,cur)



    def sql_insertdata(self,sql):
        '''插入数据'''
        cur = self.connsql()[0]
        connect = self.connsql()[1]

        if cur == None:
            self.connsql()
        try:
            cur.execute(sql)
        except Exception as e:
            self.logger.info(e)
        finally:
            if cur:
                self.closesql(cur,connect)


if __name__ == "__main__":
    handlesql = HandleSql()
    print(handlesql.sql_alldata("select * from dbuser.tbapp"))


