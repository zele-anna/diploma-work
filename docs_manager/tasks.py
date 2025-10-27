from celery import shared_task
from django.core.mail import send_mail, EmailMessage

from config.settings import EMAIL_HOST_USER
from docs_manager.models import Document
from users.models import User


@shared_task
def send_admin_notification(doc_pk):
    """Задача по отправке уведомления о загрузке документа."""
    admins = User.objects.filter(is_superuser=False, is_staff=True, is_active=True)
    email_list = []
    for admin in admins:
        email_list.append(admin.email)

    if email_list:
        document = Document.objects.get(pk=doc_pk)
        file_content = document.file.read().decode("utf-8")  # Байтовое содержимое файла
        file_name = document.file.name.split("/")[-1]
        subject = "Загружен новый документ!"
        message = "Загружен новый документ! Необходимо произвести подтверждение или отклонение."
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=EMAIL_HOST_USER,
            to=email_list,
        )

        # Прикрепляем файл
        email.attach(file_name, file_content)

        # Отправляем письмо
        email.send()
        # send_mail(subject, message, EMAIL_HOST_USER, email_list)


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
