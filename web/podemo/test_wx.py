from web.podemo.index_page import IndexPage


class TestWX:

    def setup(self):
        self.index = IndexPage()



    def test_register(self):
        # 进入注册界面
        self.index.go_register()
