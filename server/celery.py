import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_respond_task': {
        'task': 'network_model.tasks.goapi_responds',
        'schedule': crontab(minute='*/1'),  # Запуск каждую минуту
    },
}

app.autodiscover_tasks(['network_model'])

if __name__ == '__main__':
    app.start()