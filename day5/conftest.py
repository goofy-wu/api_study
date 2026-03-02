import pytest
import requests

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json"
    })
    yield s
    s.close()

@pytest.fixture(scope="session")
def best_url():
    return "https://jsonplaceholder.typicode.com/"