# coding=utf-8
import configparser


class ReadIni(object):
    def __init__(self, filename=None, node=None):
        self.file_name = filename

        if filename == None:
            self.file_name = "../config/MxcloudElement.ini"
        if node == None:
            self.node = "MxcloudElement"
        else:
            self.node = node
        self.cf = self.load_ini(self.file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value得值
    def get_value(self, key):
        try:
            data = self.cf.get(self.node, key)
            return data
        except Exception as e:
            print(e)
#
if __name__ == '__main__':
    file_name = "../config/MxcloudElement.ini"
    read_init = ReadIni(file_name)
    data  = read_init.get_value('seletearebtn')
    # print(read_init.get_value('workbenchbtn'))
    by = data.split('>')[0]

    value = data.split('>')[1]


