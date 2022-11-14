release: python manage.py makemigrations user --no-input
release: python manage.py migrate user --no-input

web: gunicorn api.wsgi
