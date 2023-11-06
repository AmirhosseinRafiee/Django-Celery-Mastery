from ..celery_config import app

@app.task(queue='tasks')
def my_task(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        raise e

def run_tasks():
    my_task.apply_async(args=(2, 0))

