import requests
import allure

URL = "https://stellarburgers.nomoreparties.site/api/auth/login"

class TestUserLogin:

    @allure.title("Проверка возможности авторизировать пользователя")
    def test_user_login(self):
        response = requests.post(URL, json={
            "email": "test.mail@yandex.ru",
            "password": "password123",
            "name": "Anna"
        })
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == "test.mail@yandex.ru"
        assert response.json()["user"]["name"] == "Anna"

    @allure.title("Проверка возможности авторизировать пользователя с некорректным паролем")
    def test_user_login_with_incorrect_password(self):
        response = requests.post(URL, json={
            "email": "test.mail@yandex.ru",
            "password": "password 1123"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя с некорректной почтой")
    def test_user_login_with_incorrect_email(self):
        response = requests.post(URL, json={
            "email": "test.m@yandex.ru",
            "password": "password123"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя с некорректным паролем и почтой")
    def test_user_login_with_incorrect_email_and_password(self):
        response = requests.post(URL, json={
            "email": "test.m@yandex.ru",
            "password": "password 123"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя без почты")
    def test_user_login_without_email(self):
        response = requests.post(URL, json={
            "password": "password123"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя без пароля")
    def test_user_login_without_password(self):
        response = requests.post(URL, json={
            "email": "test.mail@yandex.ru"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"