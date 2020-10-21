#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
class HandleInit:

    def load_ini(self):
        file_path = base_path+"/Config/server.ini"
        # print(file_path)

        cf = configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        return cf
    
    def get_value_back(self,key,node=None):
        '''
        获取ini里面的value
        '''
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(key,node)
        except Exception:
            print("没有获取到值")
            data = None
        return data

    def get_value(self,node = None,key = None):
        if node == None:
            node = 'server'
        if key == None:
            key = 'host'

        cf = self.load_ini()
        try:
            data = cf.get(node,key)
        except:
            data = None
            print("没有获取到值")
        return data

if __name__ == "__main__":
    hi = HandleInit()


    # print(hi.get_value("server","jyhost"))

    # file_path = base_path + "/Config/server.ini"
    # print(file_path)
    # cf = configparser.ConfigParser()
    # cf.read(file_path, encoding="utf-8-sig")
    # data = cf.get("server","host")
    # print(data)