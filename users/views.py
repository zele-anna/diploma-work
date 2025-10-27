from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserRegisterSerializer


class UserCreateAPIView(CreateAPIView):
    """Контроллер создания (регистрации) пользователя."""

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = True
        user.set_password(self.request.data.get("password"))
        user.save()
