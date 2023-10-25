from celery import shared_task
from time import sleep

# @shared_task
# def task1():
#     return

# @shared_task
# def task2():
#     return

@shared_task
def ts1(priority=0, queue='celery'):
    sleep(4)
    return

@shared_task
def ts2(priority=1, queue='celery:1'):
    sleep(4)
    return

@shared_task
def ts3(priority=2, queue='celery:2'):
    sleep(4)
    return

@shared_task
def ts4(priority=3, queue='celery:3'):
    sleep(4)
    return