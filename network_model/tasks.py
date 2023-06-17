from celery import shared_task
from . import celery_app, redis_conn

@shared_task
def send_email():
    pass
