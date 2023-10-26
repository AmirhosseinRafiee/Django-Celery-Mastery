import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery('dcelery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.task_routes = {
#     'newapp.tasks.task1': {'queue': 'queue1'},
#     'newapp.tasks.task2': {'queue': 'queue2'}
# }

app.conf.task_default_rate_limit = '4/m'

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
