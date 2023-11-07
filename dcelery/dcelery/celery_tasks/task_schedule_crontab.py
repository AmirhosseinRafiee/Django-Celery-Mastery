from celery.schedules import crontab
from ..celery_config import app

# app.conf.beat_schedule = {
#     'task1': {
#         'task': 'dcelery.celery_tasks.task_schedule_crontab.task1',
#         'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'),
#         'kwargs': {'foo': 'bar'},
#         'args': (2, 5),
#         'options': {
#             'queue': 'tasks',
#             'priority': 5
#         }
#     },
#     'task2': {
#         'task': 'dcelery.celery_tasks.task_schedule_crontab.task2',
#         'schedule': crontab()
#     }
# }

@app.task(queue='tasks')
def task1(a, b, **kwargs):
    result = a + b
    print('task1 is running', result)

@app.task(queue='tasks')
def task2():
    print('task2 is running')


"""
* * * * *
| | | | |
| | | | +---- Day of week (0 - 6) (Sunday=0 or 7)
| | | +------ Month (1 - 12)
| | +-------- Day of the Month (1 - 31)
| +---------- Hour (0 - 23)
+------------ Minute (0 - 59)
"""
