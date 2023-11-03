from celery import group
from celery.result import AsyncResult
from ..celery_config import app


@app.task(queue='tasks')
def task_add(number):
    if number == 4:
        raise ValueError('Number is invalid')
    else:
        return number * 2

def handle_result(result: AsyncResult):
    if result.successful():
        print('Task completed: {}'.format(result.get()))
    elif result.failed() and isinstance(result.result, ValueError):
        print('Task failed: {}'.format(result.result))
    elif result.status == 'REVOKED':
        print('Task revoked: {}'.format(result.id))

def run_tasks():
    task_group = group(task_add.s(i) for i in range(1, 6))
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)
    for result in result_group:
        handle_result(result)


