from celery import shared_task
from django.core.mail import EmailMessage
from server.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_email():
    email = EmailMessage(
        'Test email from SendGrid',
        'This is a test email from SendGrid',
        DEFAULT_FROM_EMAIL,
        ['nick.kaliga@ya.ru'],
    )
    email.send(fail_silently=False)
    send_email.apply_async(countdown=60)