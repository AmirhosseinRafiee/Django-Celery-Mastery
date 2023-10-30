import os
import time
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

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(queue='tasks')
def t1(a, b, message=None):
    result = a + b
    if message:
        result = '{} {}'.format(message, result)
    return result

@app.task(queue='tasks')
def t2():
    time.sleep(4)
    return

@app.task(queue='tasks')
def t3():
    time.sleep(4)
    return

@app.task(queue='tasks')
def t4():
    time.sleep(4)
    return

def test():
    a: AsyncResult = t1.apply_async(args=(5, 10), kwargs={'message': 'The sum is'})

    if a.ready():
        print('task has completed.')
    else:
        print('task is still running.')

    if a.successful():
        print('task completed succeeded.')
    else:
        print('task not completed succeeded (yet).')

    try:
        result = a.get()
        print('Task result:', result, a.status)
    except Exception as e:
        print('An exception occurred', str(e))
