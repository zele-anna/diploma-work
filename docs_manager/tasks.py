from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from docs_manager.models import Document


@shared_task
def send_status_notification(doc_pk, status):
    """Задача по отправке уведомления об изменении статуса документа."""
    documents = Document.objects.filter(pk=doc_pk)
    email_list = []
    for document in documents:
        email_list.append(document.owner.email)

    if email_list:
        subject = f"Документ {status}!"
        message = f"Документ, который Вы загрузили, был {status} администратором!"
        send_mail(subject, message, EMAIL_HOST_USER, email_list)
