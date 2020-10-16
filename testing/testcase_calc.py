import pytest
from testing.testing_demo import Calculator
from handle.makeCalcDatayaml import MakeCalcdata
import yaml
class TestCalc:

    def setup_module(self):
        MakeCalcdata().writeData()

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
        except TypeError as e:
            print("减法不支持的测试数据，例如：'str' and 'str'，")

    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../testdata/testyaml.yaml")))
    def testcase_mul(self,a,b):
        try:
            result = self.calc.mul(a,b)
            assert result == a * b
        except TypeError as e :
            print("乘法不支持的测试数据，例如：同str类型的乘法")

    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../testdata/testyaml.yaml")))
    def testcase_div(self,a,b):
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

