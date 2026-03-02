from conftest import *

def test_get_post(session,best_url):
    resp = session.get(best_url+"users/1")
    assert resp.status_code == 200
    assert "id" in resp.json()