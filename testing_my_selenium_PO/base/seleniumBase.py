import os

from selenium import webdriver
class SeleniumBase:
    def setup_class(self):
        browser = 'chrome'
        # browser = os.getenv("browser")
        if browser == 'chrome':
            self.option = webdriver.ChromeOptions()
            self.option.add_experimental_option('w3c',False)
            self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
            self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)
        elif browser == 'firefox':
            self.driver = webdriver.firefox()


    def teardown_class(self):
        self.driver.quit()

    # def test01(self):
    #     self.driver.get("https://www.baidu.com")

