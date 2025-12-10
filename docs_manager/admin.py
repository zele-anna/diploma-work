from django.contrib import admin, messages

from docs_manager.models import Document
from docs_manager.tasks import send_status_notification


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """Настройка отображения информации о документах в административной панели."""

    list_display = ("id", "title", "owner", "status")
    list_filter = ("status",)
    actions = ["approve", "decline"]

    @admin.action(description="Подтвердить документ")
    def approve(self, request, queryset):
        """Функция подтверждения документа в административной панели."""
        queryset.update(status="Подтвержден")
        updated_count = queryset.update(status="Подтвержден")
        self.message_user(request, f"Документов подтверждено: {updated_count}", messages.SUCCESS)
        # Отправляем уведомление об отклонении на почту.
        for doc in queryset:
            send_status_notification.delay(doc.pk, "подтвержден")

    @admin.action(description="Отклонить документ")
    def decline(self, request, queryset):
        """Функция отклонения документа в административной панели."""
        queryset.update(status="Отклонен")
        updated_count = queryset.update(status="Отклонен")
        self.message_user(request, f"Документов отклонено: {updated_count}", messages.SUCCESS)
        # Отправляем уведомление об отклонении на почту.
        for doc in queryset:
            send_status_notification.delay(doc.pk, "отклонен")

    # Наименования быстрых действий в административной панели
    approve.short_description = "Подтвердить"
    decline.short_description = "Отклонить"
