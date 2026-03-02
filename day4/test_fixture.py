from conftest import *

def test_get_post(session):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resp = session.get(url)
    assert resp.status_code == 200
    assert "id" in resp.json()