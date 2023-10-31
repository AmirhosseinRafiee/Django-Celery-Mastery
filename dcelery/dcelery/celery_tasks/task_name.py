from ..celery_config import app

@app.task
def task_test():
    pass