import numpy as np
import pytest

list1=[1,2,3,4,5,6]
array1=np.array(list1)
print(array1)

class TestData:
    def testmsplit(self):
        list = ['2782\n55500001\n55500001\n2020-10-16 15:49:04\n2020-11-05 23:59:59\n-（-）\n本周\n体验\nTeamKit\napp\n详情\n禁用\n启用', '2781\n55500000\n55500000\n2020-10-16 15:47:58\n2020-11-05 23:59:59\n-（-）\n本周\n体验\nTeamKit\napp\n详情\n禁用\n启用', '2780\n秋霖\n2020-07-15 21:53:35\n-\n-（-）\n1月前\n过期\nTeamKit\nH5\n详情\n禁用\n启用', '2779\n张立业\n15889950021\n2020-07-09 14:32:04\n2020-07-29 23:59:59\n-（-）\n1月前\n过期\nTeamKit\napp\n详情\n禁用\n启用', '2778\n13200000042\n13200000042\n2020-05-27 11:27:08\n2020-06-16 23:59:59\n-（-）\n1月前\n过期\nTeamKit\napp\n详情\n禁用\n启用', '2777\n13200000040\n13200000040\n2020-05-27 11:14:01\n2020-06-16 23:59:59\n20200527创建（-）\n1月前\n过期\nTeamKit\napp\n详情\n禁用\n启用', '2776\n13200000041\n13200000041\n2020-05-27 11:13:10\n2020-06-16 23:59:59\n20200527创建（-）\n1月前\n过期\nTeamKit\napp\n详情\n禁用\n启用', '2775\nwj\n13602571111\n2020-05-26 18:20:28\n2020-06-15 23:59:59\n-（测试团队222）\n-\n过期\nTeamKit\n-\n详情\n禁用\n启用', '2774\n石成的电信卡一号😀ོ\n13316544625\n2020-05-26 17:50:50\n2020-06-15 23:59:59\n-（-）\n1月前\n过期\nTeamKit\nH5、小程序\n详情\n禁用\n启用', '2773\nhfivestar\n2020-05-19 09:26:30\n-\n-（-）\n1月前\n过期\nTeamKit\nH5\n详情\n禁用\n启用']
        slist = []
        # print(list)
        for ili in list:
            ili = ili.split(',')
            slist.append(ili)


        list = []
        for i in range(0,len(slist) - 1):
            a = slist[i][0].split('\n')
            # print(a)
            list.append(a)
        print(list)

        print(list[0][0])
        print(list[0][1])



if __name__ == '__main__':
    print(TestData().testmsplit())


