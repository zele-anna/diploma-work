from django.db import models

from users.models import User


class Document(models.Model):
    """Модель документа."""

    UPLOADED = "Загружен"
    APPROVED = "Подтвержден"
    DECLINED = "Отклонен"

    STATUS_CHOICES = [
        (UPLOADED, UPLOADED),
        (APPROVED, APPROVED),
        (DECLINED, DECLINED),
    ]

    title = models.CharField(max_length=255, verbose_name="Наименование документа")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Владелец", blank=True, null=True)
    file = models.FileField(upload_to="docs_manager/uploads", verbose_name="Файл")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name="Статус документа", default=UPLOADED)
    uploaded_at = models.DateTimeField(verbose_name="Дата и время загрузки", auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name="Дата и время обновления", default=None, blank=True, null=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title
