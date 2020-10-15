import pytest
from testing.testing_demo import Calculator
import random

class TestCalc:

    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")


    def teardown_class(self):
        print("计算结束")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")


    @pytest.mark.parametrize('a,b,expect',
                             [[0,0,0],[1,1,2],[100,100,200],[0.1,0.1,0.2],[-1,-1,-2],
                              [10000000000,100000000,10100000000],[100,-1000,-900]],
                             ids = ['zero_case','int_case','bignum_case','float_case',"minus_case","bignum_case","intminus_case"])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    def test_add_01(self):

        a = random.uniform(-1000000000000,1000000000000)
        b = random.uniform(-1000000000000,1000000000000)
        expect = a + b

        result = self.calc.add(a,b)
        assert result == expect

    def test_add_02(self):
        a = random.choice("abcdefghijklmnopqrstuvwxyz!@#$%^&*()")
        b = random.choice("abcdefghijklmnopqrstuvwxyz!@#$%^&*()")

        assert self.calc.add(a,b) == a + b

    def test_add_03(self):
        a = [1,2,3,4,5]
        b = [1,2]
        assert self.calc.add(a,b) == [1, 2, 3, 4, 5, 1, 2]

    def test_add_04(self):
        a = ( 'AAAANNI', 786 , 2.23, 'john', 70.2 )
        b = ( 'AAAAeeNNI', 7286 , 2.23, 'joehn', 70.2 )
        assert self.calc.add(a,b) == a + b







