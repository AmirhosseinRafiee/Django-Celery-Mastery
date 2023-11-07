from datetime import timedelta
from ..celery_config import app

# app.conf.beat_schedule = {
#     'task1': {
#         'task': 'dcelery.celery_tasks.task_schedule_customization.task1',
#         'schedule': timedelta(seconds=5),
#         'kwargs': {'foo': 'bar'},
#         'args': (2, 5),
#         'options': {
#             'queue': 'tasks',
#             'priority': 5
#         }
#     },
#     'task2': {
#         'task': 'dcelery.celery_tasks.task_schedule_customization.task2',
#         'schedule': timedelta(seconds=10)
#     }
# }

@app.task(queue='tasks')
def task1(a, b, **kwargs):
    result = a + b
    print('task1 is running', result)

@app.task(queue='tasks')
def task2():
    print('task2 is running')
