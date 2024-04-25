#!/bin/sh
#poetry run python coworkingspace\manage.py ldap_sync_users;
#poetry run python coworkingspace\manage.py ldap_promote cwadmin;
#poetry run python manage.py migrate;
#poetry run gunicorn -w 2 -b 0.0.0.0:8000 coworkingspace.coworkingspace.wsgi:application;
#poetry run python manage.py createsuperuser --noinput;

poetry run python3 manage.py migrate;
poetry run python3 manage.py ldap_sync_users;
poetry run python3 manage.py ldap_promote cwadmin;
poetry run python3 manage.py createsuperuser --noinput;
poetry run gunicorn -w 2 -b 0.0.0.0:8000 coworkingspace.wsgi:application;
