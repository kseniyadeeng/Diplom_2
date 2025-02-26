import pytest
import requests

from Urls import *
from data import *

@pytest.fixture(scope="function")
def user_login():
    login_response = requests.post(URL_2, json = test_data)
    assert login_response.status_code == 200
    assert login_response.status_code == 200
    access_token = login_response.json()["accessToken"]
    yield access_token

@pytest.fixture(scope="function")
def user_registration_and_delete():
    response = requests.post(URL_3, json=test_data_2)
    assert response.status_code == 200
    assert response.json()["success"] is True

    access_token = response.json()["accessToken"]
    yield access_token

    delete_response = requests.delete(URL, headers={"Authorization": access_token})
    assert delete_response.status_code == 202
    assert delete_response.json()["success"] is True