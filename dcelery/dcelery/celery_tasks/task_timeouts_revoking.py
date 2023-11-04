from time import sleep
from billiard import exceptions as billiard_exceptions
from celery import exceptions as celery_exceptions
from celery.result import AsyncResult
from ..celery_config import app

@app.task(queue='tasks', time_limit=10)
def long_running_task():
    sleep(5)
    return 'Task completed successfully.'

def execute_task_examples():
    result = long_running_task.delay()
    try:
        result = result.get(timeout=20)
    except celery_exceptions.TimeoutError:
        print('Task timed out')
    except billiard_exceptions.TimeLimitExceeded:
        print('Task time limit exceeded')

    task: AsyncResult = long_running_task.delay()
    task.revoke(terminate=True)

    sleep(2)
    print(task.status)
