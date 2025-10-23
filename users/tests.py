from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тестирование операций с пользователями."""

    def setUp(self):
        self.user = User.objects.create(email="test1@example.com")

    def test_user_create(self):
        """Тест на создание пользователя."""
        url = reverse("users:register")
        data = {"email": "test@user.com", "password": "12345"}
        response = self.client.post(url, data=data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверка записи в БД
        self.assertEqual(User.objects.all().count(), 2)
        # Проверка вывода строкового значения
        self.assertEqual(str(self.user), "test1@example.com")
