import os

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from config.settings import MEDIA_ROOT
from docs_manager.models import Document
from users.models import User


class DocumentTestCase(APITestCase):
    """Тестирование операций по классу Document."""

    def setUp(self):
        self.user = User.objects.create(email="test1@example.com")
        self.file_name = "test_file.txt"
        self.file_content = b"This is a test file content."

        # Создание фиктивного файла
        with open(self.file_name, "wb") as f:
            f.write(self.file_content)
        self.client.force_authenticate(user=self.user)

    def test_doc_upload_success(self):
        """Тест на загрузку документа."""
        url = reverse("docs_manager:upload")
        with open(self.file_name, "rb") as f:
            data = {"title": "Doc test upload", "file": f}
            response = self.client.post(url, data=data, format="multipart")

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверка записи в БД
        self.assertEqual(Document.objects.all().count(), 1)
        # Проверка пути к файлу
        expected_file_path = os.path.join(MEDIA_ROOT, "docs_manager", "uploads", self.file_name)
        self.assertTrue(os.path.exists(expected_file_path))
        # Проверка вывода строкового значения
        self.document = Document.objects.get(title="Doc test upload")
        self.assertEqual(str(self.document), "Doc test upload")

    def tearDown(self):
        # Удаление фиктивного файла после теста
        path = os.path.join(MEDIA_ROOT, "docs_manager", "uploads", self.file_name)
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(self.file_name):

            os.remove(self.file_name)
