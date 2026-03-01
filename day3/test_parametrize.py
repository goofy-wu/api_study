import pytest
import requests


@pytest.mark.parametrize("user_id",[1,2,3])
def test_get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    r = requests.get(url)
    data = r.json()

    assert r.status_code == 200
    assert "id" in data
    assert data["id"] == user_id

@pytest.mark.parametrize(
    "a,b,expect",
    [
        (1,2,3),
        (2,2,4),
        (2,3,5)
    ]

)
def test_add(a,b,expect):
    result = a + b
    assert result == expect
