import pytest

@pytest.fixture(autouse=True,scope="function",params=['jerry'])
def login(request):
    print("登录")
    username = request.param
    yield  username # 相当于return
    # yield 前面的操作相当于 setup ,yield 后面的操作相当于teardown
    print("登出")

@pytest.fixture(scope="session")
def connect_db():
    print("连接数据库")

