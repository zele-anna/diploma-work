from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор пользовательской информации."""

    class Meta:
        model = User
        fields = (
            "pk",
            "email",
        )
