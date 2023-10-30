pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
docker compose exec django sh -c "python manage.py startapp worker"
docker compose exec -it django sh -c "python manage.py shell"
from newapp.tasks import ts1, ts2, ts3, ts4
ts1.delay()
from celery import group, chain
from newapp.tasks import ts1, ts2, ts3, ts4
task_group = group(ts1.s(), ts2.s(), ts3.s(), ts4.s())
task_group.apply_async()
task_chain = chain(ts1.s(), ts2.s(), ts3.s(), ts4.s())
task_group.apply_async()
from dcelery.celery import t1, t2, t3, t4
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t4.apply_async(arg=(4, 6), kwargs=(message='test message'))