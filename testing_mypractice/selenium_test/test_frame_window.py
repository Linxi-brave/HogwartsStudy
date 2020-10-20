from selenium import webdriver
from testing_mypractice.selenium_test.seleniumbase import SeleniumBase
class TestWindows(SeleniumBase):
    '''
    窗口切换：
    点击某些链接的时候，会跳转到另外一个窗口，这个时候就需要使用切换窗口的操作了
    driver.current_window_handle # 当前窗口
    driver.window_handles # 所有窗口
    sriver.switch_to_windows[0]  # 切换窗口
    frame 切换：
    如果元素定位不到，应该位于frame中，需要切换到对应的frame进行定位元素
    driver.switch_to_frame("frameId") # 切换到对应的frame下
    driver.switch_to.parent_frame()   # 在当前frame切换到父frame节点下
    driver.switch_to_default_content() # 切换到默认的frame节点
    '''

    def test_windows(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle) # 打印当前窗口
        print(self.driver.window_handles)  # 所有窗口
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1]) # 切换当前窗口
        # 进行该界面的操作后，再切换窗口
        self.driver.switch_to_window(windows[0]) # 切换当前窗口


    def test_frame(self):
        self.driver.get()
        self.driver.switch_to_frame("frameId") # 切换到对应frame 下
        self.driver.switch_to.parent_frame() # 切回到父frame 节点
        self.driver.switch_to_default_content() #   切换回默认的frame节点
        self.driver.switch_to_alert().accept() # 点击alert上面的同意
        self.driver.switch_to_alert().dismiss() # 点击alert上面的拒绝