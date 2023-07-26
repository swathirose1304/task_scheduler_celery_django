from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler_project.settings')

app = Celery('scheduler_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata') 

app.config_from_object(settings, namespace='CELERY')   

# Celery Beat Settings
app.conf.beat_schedule = {
      'send-mail-every-day-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=16, minute=10) #day_of_month=21,month_of_year = 7),
        #'args': (2,)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
