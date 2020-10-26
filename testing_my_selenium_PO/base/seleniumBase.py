import os

from selenium import webdriver
class SeleniumBase:
    def setup_class(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('w3c', False)
        self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'

        browser = 'debug'
        # browser = os.getenv("browser")
        if browser == 'chrome':
            self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)

        elif browser == 'firefox':
            self.driver = webdriver.firefox()

        elif browser == "debug":
            self.option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            self.driver = webdriver.Chrome(options=self.option, executable_path=self.path)

            self.driver.implicitly_wait(2)
            self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def test01(self):
        self.driver.get("https://home.bitkinetic.com/activity")


