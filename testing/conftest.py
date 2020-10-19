import pytest
import yaml

from pythoncode.testing_demo import Calculator

@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    print("【开始计算】")
    yield calc
    print("【计算结束】")


def pytest_collection_modifyitems(items):
    # print("收集到的测试用例",items)

    #控制用例执行顺序：加 - 除 - 减 - 乘
    new_items = ['testcase_add','testcase_div','testcase_sub','testcase_mul']
    items = new_items

    print('修改后的测试用例集合',items)

if __name__ == '__main__':
    pytest.main(['-s'])