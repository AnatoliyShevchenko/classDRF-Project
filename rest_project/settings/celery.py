# Python
from os import environ
from decouple import config

# Third party
from celery import Celery
from celery.schedules import crontab

# Django
from django.conf import settings


environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
app: Celery = Celery(
    'settings',
    broker=settings.CELERY_BROKER_URL,
    include=(
        'main.tasks',
    )
)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'every-1-minute-every-day': {
        'task': 'change-player-age',
        'schedule': crontab(minute='*/60')
    },
    # 'every-minute-every-day' : {
    #     'task' : 'sending-raport',
    #     'schedule' : crontab(month_of_year='*/1')
    # },
}
app.conf.timezone = 'UTC'