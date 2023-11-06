from celery.signals import task_failure
from ..celery_config import app

@app.task(queue='tasks')
def cleanup_failed_task(task_id, *args, **kwargs):
    print("CLEAN UP", task_id)

@app.task(queue='tasks')
def my_task():
    raise ValueError('Task failed')

@task_failure.connect(sender=my_task)
def handle_task_failure(sender=None, task_id=None, *args, **kwargs):
    cleanup_failed_task.apply_async(args=(task_id,))

def run_tasks():
    my_task.apply_async()
