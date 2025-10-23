from rest_framework.serializers import ModelSerializer

from docs_manager.models import Document


class DocumentSerializer(ModelSerializer):
    """Стандартный сериализатор документа - сериализация всех полей."""

    class Meta:
        model = Document
        fields = "__all__"
