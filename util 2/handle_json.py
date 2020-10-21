import json
import os
base_path = os.getcwd()

class HandleJson:

    def __init__(self):
        self.file_path = None

    def read_json(self,file_name):
        with open(file_name,encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_value(self,key,file_path):
        data = self.read_json(file_path)
        return data[key]

    def write_value(self,data,file_path):
        data_value = json.dumps(data)
        with open(file_path,"w") as f:
            f.write(data_value)

if __name__ == '__main__':
    handleJson = HandleJson()

    data = {
        "app":{
            "aaaa":"bbbbbb"
        }
    }
    file_name = '../data/data.json'
    handleJson.write_value(data,file_name)
    json = handleJson.read_json(file_name)



