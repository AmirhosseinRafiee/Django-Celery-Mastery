pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
docker compose exec django sh -c "python manage.py startapp worker"
docker compose exec -it django sh -c "python manage.py shell"
from newapp.tasks import ts1, ts2, ts3, ts4
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts1.delay()
ts2.delay()
ts3.delay()
ts4.delay()
ts1.delay()
ts2.delay()
ts3.delay()
ts4.delay()
ts1.delay()
ts2.delay()
ts3.delay()
ts4.delay()
ts1.delay()
ts2.delay()
ts3.delay()
ts4.delay()