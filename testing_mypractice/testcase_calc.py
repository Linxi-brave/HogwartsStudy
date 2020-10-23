import shelve

import pytest
from pythoncode.testing_demo import Calculator
from util.handle_yaml import HandleYaml
import yaml


def get_datas():
    '''
    :return: 解析测试数据的函数，从yaml文件中读取测试数据
    '''
    with open("../testdata/calc.yaml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        adds_data = datas['add']['datas']
        adds_id = datas['add']["ids"]

        return [adds_data,adds_id]

def steps(calc,a,b,expect,stepfile):
    '''
    :param calc:
    :param a: add 函数中的一个加法参数
    :param b: add 函数中的一个加法参数
    :param expect: add 函数中的预期结果
    :param stepfile: 传入存有测试步骤的yaml文件路径
    :return: 解析测试步骤的函数，从yaml文件中读取测试步骤
    '''

    with open(stepfile) as f:
        steps = yaml.safe_load(f)

        for step in steps:
            if 'add' == step:
                result = calc.add(a,b)
                print("执行 add")
            elif 'add1' == step :
                result = calc.add1(a,b)
                print("执行 add1")
            assert  expect == result

@pytest.fixture(scope="class")
def get_calc():
    print("打印开始计算")
    calc = Calculator()
    yield calc
    print("打印结束计算")

class TestCalc2:
    @pytest.mark.parametrize('a,b,expec',get_datas()[0],ids = get_datas()[1])
    def testcase_add(self,a,b,get_calc,expec):
        result = get_calc.add(a,b)
        assert result == expec

class TestCalc:

    def setup_module(self):
        HandleYaml().writeData()

    def setup_class(self):
        self.calc = Calculator()
    def teardown_class(self):
        pass

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../testdata/testyaml.yaml")))
    def testcase_add(self,a,b):
        result = self.calc.add(a,b)
        assert result == a + b

    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../testdata/testyaml.yaml")))
    def testcase_sub(self,a,b):
        try:
            result = self.calc.sub(a,b)
            assert result == a - b
        except TypeError :
            print("减法不支持的测试数据，例如：'str' and 'str'，")

    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../testdata/testyaml.yaml")))
    def testcase_mul(self,a,b):
        try:
            result = self.calc.mul(a,b)
            assert result == a * b
        except TypeError  :
            print("乘法不支持的测试数据，例如：同str类型的乘法")

    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../testdata/testyaml.yaml")))
    def testcase_div(self,a,b):
        # 使用 pytest.raises(ZeroDivisionError) 抛出异常时，如果没有抛出异常，则测试用例会报错
        # with pytest.raises(ZeroDivisionError):
        #     self.calc.div(a,b)
        try:
            result = self.calc.div(a,b)

            assert result == a / b
        except TypeError :
            print("除法不支持的测试数据，例如：同str类型")
        except ZeroDivisionError :
            print("除数为0情况")

    def testcase_listdata(self):
        a = [1, 2, 3, 4, 5]
        b = [1, 2]
        assert self.calc.add(a, b) == [1, 2, 3, 4, 5, 1, 2]

    def testcase_tupledata(self):
        a = ('AAAANNI', 786, 2.23, 'john', 70.2)
        b = ('AAAAeeNNI', 7286, 2.23, 'joehn', 70.2)
        assert self.calc.add(a, b) == a + b

    @pytest.mark.parametrize('a,b,expect',[[0.1,0.2,0.3],[0.2,0.2,0.4]])
    def testcase_add_float(self,a,b,expect):
        result = self.calc.add(a,b)
        assert round(result,2) == expect

    @pytest.mark.parametrize('a,b',[[0,1],[0,0.5]])
    def testcase_div_zero(self,a,b):
        result = self.calc.div(a,b)
        assert result == 0

    @pytest.mark.parametrize('a,b,expec',get_datas()[0],ids = get_datas()[1])
    def testcase_param_add(self,a,b,expec):
        result = self.calc.add(a,b)
        assert result == expec

    @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids = get_datas()[1])
    def test_add_step(self,a,b,expect):
        steps(self.calc,a,b,expect,'./steps/add_steps.yaml')


    # @pytest.mark.skip
    def testshelve(self):
        cookies = '1111111'
        db = shelve.open("cookies")
        db.cookies = cookies
        db.close()
        mcookies = db.get("cookies")
        print(mcookies)