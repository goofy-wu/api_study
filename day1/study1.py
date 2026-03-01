import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    r = requests.get(url)

    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    r = requests.get(url)

    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    #提交参数
    data = {
        "title": "test",
        "body": "hello",
        "userId":1
    }
    r = requests.post(url, json=data)

    assert r.status_code == 201
    assert r.json()["title"] == "test"

if __name__ == '__main__':
    test_create_post()
    test_get_user()
    test_get_post()
