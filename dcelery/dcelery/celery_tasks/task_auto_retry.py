import logging
from celery import Task
from ..celery_config import app

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class MyTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection error occurred.')
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))

# app.Task = MyTask

@app.task(queue='tasks', base=MyTask, autoretry_for=(ConnectionError,),  retry_kwargs={'max_retries': 4, 'countdown': 5})
def my_task():
    raise ConnectionError('Connection error occurred.....')
    return
