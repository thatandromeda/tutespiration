import os

from .base import *

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

PROTO_DEBUG = os.environ.get('DJANGO_DEBUG', None)
if PROTO_DEBUG:
    DEBUG = True
else:
    DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
