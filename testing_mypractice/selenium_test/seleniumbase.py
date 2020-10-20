from selenium import webdriver
import os

class SeleniumBase():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'chrome':
            self.option = webdriver.ChromeOptions()
            self.option.add_experimental_option('w3c', False)
            self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
            self.driver = webdriver.Chrome(options=self.option, executable_path=self.path)
        elif browser == 'firefox':
            self.driver = webdriver.firefox()

        self.driver.implicitly_wait(2)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()