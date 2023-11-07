from datetime import timedelta
from ..celery_config import app

# app.conf.beat_schedule = {
#     'task1': {
#         'task': 'dcelery.celery_tasks.task_schedule.task1',
#         'schedule': timedelta(seconds=5)
#     },
#     'task2': {
#         'task': 'dcelery.celery_tasks.task_schedule.task2',
#         'schedule': timedelta(seconds=10)
#     }
# }

@app.task(queue='tasks')
def task1():
    print('task1 is running')

@app.task(queue='tasks')
def task2():
    print('task2 is running')
