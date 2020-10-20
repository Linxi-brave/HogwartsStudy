from testing_mypractice.selenium_test.seleniumbase import SeleniumBase
class TestJs(SeleniumBase):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("测试")
        element = self.driver.execute_script("return document.getElementbyId('su')")
        element.send_keys()
        element.click()

    '''
    文件上传：input标签可以使用send_keys(文件地址)进行上传文件
    用法：ele.send_keys(filepath)
    '''