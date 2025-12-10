from django.urls import path

from docs_manager.apps import DocsManagerConfig
from docs_manager.views import DocumentCreateAPIView

app_name = DocsManagerConfig.name


urlpatterns = [
    path("upload/", DocumentCreateAPIView.as_view(), name="upload"),
]
