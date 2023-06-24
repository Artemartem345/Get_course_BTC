import os
from celery import Celery
from django.conf import settings



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Btc_course.settings")

app = Celery('Btc_course')

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()