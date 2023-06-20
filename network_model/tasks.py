from celery import shared_task
from . import celery_app, redis_client

@shared_task
def send_email():
    pass
