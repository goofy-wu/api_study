import pytest
import requests

@pytest.fixture(scope="session")
def session():
    # 创建一个 session 对象
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json"
    })
    yield s     # 返回 session 对象
    s.close()   # 测试结束后关闭 session