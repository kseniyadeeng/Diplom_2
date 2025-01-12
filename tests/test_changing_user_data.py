import requests
import allure

URL = "https://stellarburgers.nomoreparties.site/api/auth/user"
URL2 = "https://stellarburgers.nomoreparties.site/api/auth/login"

class TestChangingUserData:

    @allure.title("Проверка возможности смены имени у авторизированного пользователя")
    def test_changing_name_user_with_login(self):

        login_response = requests.post(URL2, json={
            "email": "test.mail@yandex.ru",
            "password": "password123"
        })
        assert login_response.status_code == 200
        access_token = login_response.json()["accessToken"]

        response = requests.patch(
            URL,
            json={"email": "test.myau@yandex.ru", "name": "Lerochka"},
            headers={"Authorization": access_token}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == "test.mail@yandex.ru"
        assert response.json()["user"]["name"] == "Anna"

    @allure.title("Проверка возможности смены почты у авторизированного пользователя")
    def test_changing_email_user_with_login(self):

        login_response = requests.post(URL2, json={
            "email": "test.mail@yandex.ru",
            "password": "password123"
        })
        assert login_response.status_code == 200
        access_token = login_response.json()["accessToken"]

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