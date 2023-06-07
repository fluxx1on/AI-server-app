from celery import shared_task
from django.core.mail import EmailMessage
from server.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_email():
    