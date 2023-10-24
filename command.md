pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
docker compose exec django sh -c "python manage.py startapp worker"