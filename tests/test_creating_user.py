import pytest
import requests
from helpers import *
import allure
from conftest import *
from Urls import *
from data import *

class TestUserRegistration:

    @allure.title("Проверка возможности зарегистрировать пользователя")
    def test_user_registration(self, user_registration_and_delete):

        login_response = requests.post(URL_2, json={
            "email": test_data_2["email"],
            "password": test_data_2["password"]
        })

        assert login_response.status_code == 200
        assert login_response.json()["user"]["email"] == test_data_2["email"]
        assert login_response.json()["user"]["name"] == test_data_2["name"]

    @allure.title("Проверка возможности зарегистрировать уже зарегистрированного пользователя")
    def test_creating_registered_user(self):
        response = requests.post(URL_3, json= {"email": "test.myau@yandex.ru","password": "cool password", "name": "Lerochka"})
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Проверка возможности зарегистрировать пользователя без почты")
    def test_user_registration_without_email(self):
        response = requests.post(URL_3, json={
            "password": "password123",
            "name": "Anna"
        })
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Проверка возможности зарегистрировать пользователя без пароля")
    def test_user_registration_without_password(self):
        response = requests.post(URL_3, json={
            "email": "test.no_password@yandex.ru",
            "name": "Anna"
        })
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Проверка возможности зарегистрировать пользователя без имени")
    def test_user_registration_without_name(self):
        response = requests.post(URL, json={
            "email": "test.no_name@yandex.ru",
            "password": "password123"
        })
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"