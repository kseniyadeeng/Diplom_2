import pytest
import requests

from Urls import *
from data import *

@pytest.fixture(scope="function")
def user_login():
    login_response = requests.post(URL2, json = test_data)
    assert login_response.status_code == 200
    assert login_response.status_code == 200
    access_token = login_response.json()["accessToken"]
    yield access_token
