import requests
import allure
from Urls import *
from data import *
from conftest import *


class TestChangingUserData:

    @allure.title("Проверка возможности смены имени у авторизированного пользователя")
    def test_changing_name_user_with_login(self, user_login):
        access_token = user_login
        response = requests.patch(
            URL,
            json={"email": "test.mail@yandex.ru", "name": "Lerochka"},
            headers={"Authorization": access_token}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == "test.mail@yandex.ru"
        assert response.json()["user"]["name"] == "Anna"

    @allure.title("Проверка возможности смены почты у авторизированного пользователя")
    def test_changing_email_user_with_login(self, user_login):

        access_token = user_login
        response = requests.patch(
            URL,
            json={"email": "test.mail@yandex.ru", "name": "Anna"},
            headers={"Authorization": access_token}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == "test.mail@yandex.ru"
        assert response.json()["user"]["name"] == "Anna"

    @allure.title("Проверка возможности смены имени у не авторизированного пользователя")
    def test_changing_name_user_without_login(self):

        response = requests.patch(
            URL,
            json={"email": "test.mail@yandex.ru", "name": "Anna"}
        )
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "You should be authorised"

    @allure.title("Проверка возможности смены почты у не авторизированного пользователя")
    def test_changing_email_user_without_login(self):

        response = requests.patch(
            URL,
            json={"email": "test.mail@yandex.ru", "name": "Anna"}
        )
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "You should be authorised"