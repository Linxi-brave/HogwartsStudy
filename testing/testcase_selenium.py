import shelve

from selenium import  webdriver
class TestcaseSelenium():

    def setup(self):

        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("w3c",False)

        self.path = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver'
        self.driver = webdriver.Chrome(options=self.option,executable_path=self.path)

        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


    def testcasegetcookie(self):
        url = ''
        self.driver.get(url)
        cookies = self.driver.get_cookies()
        db = shelve.open("cookies")
        db.cookies = cookies
        db.close()

    def testcaseselenium(self):
        self.url = ""
        db = shelve.open("cookies")
        cookie = db.get("cookies")
        db.close()
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.get(self.url)


