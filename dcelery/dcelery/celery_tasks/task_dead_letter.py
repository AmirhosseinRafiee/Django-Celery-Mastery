from celery import group
from ..celery_config import app

app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True

@app.task(queue='tasks')
def my_task(n):
    try:
        if n == 2:
            raise ValueError('Error: Wrong number')
    except Exception as e:
        handle_failed_task.apply_async(args=(n, str(e)))
        raise


@app.task(queue='dead_letter')
def handle_failed_task(n, exception):
    return "Custom logic to process"

def run_task_group():
    task_group = group(my_task.s(i) for i in range(1, 5))
    task_group.apply_async()
