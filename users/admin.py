from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройка отображения пользователей в административной панели."""

    list_display = ("id", "email")
