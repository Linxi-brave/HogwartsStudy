import yaml
import random
class MakeCalcdata:
    '''
    生成Calc测试用例的测试数据，并将测试数据写入到../testdata/testyaml.yaml 中
    '''

    def writeData(self):
    # 写入测试数据
        list = [[0,0]]
        for i in range(1,10):
            intdata = random.randint(0,10000000)
            mintdata = random.randint(-1000000000,0)
            floatdata = random.uniform(0,1000000000)
            minusfloatdata = random.uniform(-10000000,0)
            chardata = random.choice("abcdefghijklmnopqrstuvwxyz!@#$%^&*()")
            list.append([intdata,mintdata])
            list.append([intdata,floatdata])
            list.append([intdata,minusfloatdata])
            list.append([mintdata,floatdata])
            list.append([mintdata,minusfloatdata])
            list.append([floatdata,minusfloatdata])
            list.append([chardata,chardata])
        # list.append([[1, 2, 3, 4, 5, 1, 2],[1,2]])
        # list.append([( 'AAAANNI', 786 , 2.23, 'john', 70.2 ),( 'AAAANNI', 786 , 70.2 )])

        print(list)


        with open("../testdata/testyaml.yaml","w",encoding="utf-8") as f:
            yaml.dump(list,f,Dumper=yaml.Dumper)

if __name__ == '__main__':

    MakeCalcdata().writeData()