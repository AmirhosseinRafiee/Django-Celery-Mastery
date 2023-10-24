from celery import shared_task

@shared_task
def test_task_from_app():
    return