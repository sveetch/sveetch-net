"""
Settings to use for development
"""
from settings import *

# Enable django-debug-toolbar for the following IPs
INTERNAL_IPS = ('192.168.0.112',)

# Databases access
DATABASES = {
    'default': {
        'NAME': 'sveetchnet',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '',
        'PASSWORD': '',
    }
}

# Test emails by looking at the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
