import requests
import allure
from Urls import *

class TestCreateAnOrders:

    @allure.title("Проверка возможности создания заказа с одним ингредиентом у не авторизированного пользователя")
    def test_creating_an_order_with_one_ingredient_without_login(self):
        response = requests.post(URL_4, json={
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        })
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == "Флюоресцентный бургер"

    @allure.title("Проверка возможности создания заказа с несколькими ингредиентами")
    def test_creating_an_order_with_ingredients(self):
        response = requests.post(URL_4, json={
            "ingredients": ["61c0c5a71d1f82001bdaaa73","61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa7a"]
        })
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == "Space био-марсианский астероидный бургер"

    @allure.title("Проверка возможности создания заказа без ингредиентов")
    def test_creating_an_order_without_ingredients(self):
        response = requests.post(URL_4, json={
            "ingredients": []
        })
        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Проверка возможности создания заказа с некорректным названием ингредиентов")
    def test_creating_an_order_with_incorrect_ingredient(self):
        response = requests.post(URL_4, json={
            "ingredients": ["60d3b41abdacab006ga7463c6"]
        })
        assert response.status_code == 500

    @allure.title("Проверка возможности создания заказа с одним ингредиентом у авторизированного пользователя")
    def test_creating_an_order_with_one_ingredient_with_login(self):

        login_response = requests.post(URL_2, json={
            "email": "test.mail@yandex.ru",
            "password": "password123"
        })
        assert login_response.status_code == 200
        access_token = login_response.json()["accessToken"]

        order_response = requests.post(
            URL_4,
            json={"ingredients": "61c0c5a71d1f82001bdaaa6d"},
            headers={"Authorization": access_token}
        )

        assert order_response.status_code == 200
        assert order_response.json()["success"] is True
        assert order_response.json()["name"] == "Флюоресцентный бургер"