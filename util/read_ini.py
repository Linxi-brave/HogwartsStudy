# coding=utf-8
import configparser
from util.user_log import UserLog
import os
# parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))

class ReadIni(object):
    def __init__(self, filename=None, node=None):
        self.file_name = filename
        self.logger = UserLog().get_log()
        if filename == None:
            self.file_name = parent_dir + "/config/Element.ini"
            print(self.file_name)

        if node == None:
            self.node = "Element"
        else:
            self.node = node
        print(self.node)
        print(self.file_name)
        self.cf = self.load_ini(self.file_name)
        print(self.cf)
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value得值
    def get_value(self, key):
        print(self.node)
        print(key)
        try:
            data = self.cf.get(self.node, key)
            print(data)
            return data
        except Exception as e:
            self.logger.info(e)
#
if __name__ == '__main__':

    read_init = ReadIni()
    data  = read_init.get_value('zhzxspan')
    by = data.split('>')[0]

    value = data.split('>')[1]
    print(by)
    print(value)

