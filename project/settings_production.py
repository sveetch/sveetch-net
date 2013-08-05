# Import
from project.settings import *


DEBUG = False
ASSETS_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',               # Set to empty string for localhost.
        'PORT': '',               # Set to empty string for default.
    }
}
