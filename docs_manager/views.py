from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from docs_manager.models import Document
from docs_manager.pagination import CustomPagination
from docs_manager.serializers import DocumentSerializer


class DocumentCreateAPIView(CreateAPIView):
    """Класс для загрузки документа."""

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Присвоение пользователя в качестве владельца документа."""
        document = serializer.save()
        document.owner = self.request.user
        document.save()
