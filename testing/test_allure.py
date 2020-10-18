
import allure
# pip install allure-pytest
import pytest

@allure.feature('登录模块')
class Testlogin():

    @allure.story('登录成功')
    @pytest.mark.login
    def test_login_success(self):
        print("登录成功测试用例：登录成功")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("登录失败测试用例：登录失败")
        pass

    @allure.story('用户名缺失')
    def test_login_nousername(self):
        with allure.step("未输入用户名"):
            print("未输入用户名")

        with allure.step("输入密码"):
            print("输入密码")

        with allure.step("点击登录"):
            print("点击登录")


@allure.feature("登录模块2")
class TestLogin2():
    @allure.story('登录成功')
    def test_login_success(self):
        print("登录成功测试用例：登录成功")
        pass
