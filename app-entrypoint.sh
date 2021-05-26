python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:82
# gunicorn SAP.wsgi:application --bind 0.0.0.0:8081
