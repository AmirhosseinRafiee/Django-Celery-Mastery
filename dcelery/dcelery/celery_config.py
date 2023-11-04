import os
import time
from django.conf import settings
from celery import Celery
from celery.result import AsyncResult
from kombu import Exchange, Queue

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery('dcelery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter', Exchange('dead_letter'), routing_key='dead_letter')
]
app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

# app.conf.task_routes = {
#     'newapp.tasks.task1': {'queue': 'queue1'},
#     'newapp.tasks.task2': {'queue': 'queue2'}
# }

# app.conf.task_default_rate_limit = '4/m'

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }

base_path = os.getcwd()
tasks_path = os.path.join(base_path, 'dcelery', 'celery_tasks')
if os.path.exists(tasks_path) and os.path.isdir(tasks_path):
    task_modules = list()
    for filename in os.listdir(tasks_path):
        if filename.startswith('task') and filename.endswith('.py'):
            module_name = f'dcelery.celery_tasks.{filename[:-3]}'
            module = __import__(module_name, fromlist=['*'])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith('task'):
                    task_modules.append(f'{module_name}.{name}')
    app.autodiscover_tasks(task_modules)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
