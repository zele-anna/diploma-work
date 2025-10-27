from rest_framework.serializers import ModelSerializer

from users.models import User


class UserRegisterSerializer(ModelSerializer):
    """Сериализатор для регистрации пользователя."""

    class Meta:
        model = User
        fields = ("pk", "email", "password")
