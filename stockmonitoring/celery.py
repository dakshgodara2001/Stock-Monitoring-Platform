from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
import requests
from dotenv import load_dotenv
from mainapp.views import get_alpha_vantage_quote

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockmonitoring.settings')

app = Celery('stockmonitoring')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')