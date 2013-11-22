"""
Settings for production environment
"""
from project.settings import *

DEBUG = TEMPLATE_DEBUG = False

ASSETS_DEBUG = False
ASSETS_ROOT = STATIC_ROOT
ASSETS_AUTO_BUILD = False

# Fast-cgi options
FCGI_OPTIONS = {
    'method': 'threaded',
    'daemonize': 'false',
}

# SMTP Settings to send Applications emails
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[sveetch.net] '

# Database access
DATABASES = {
    'default': {
        'HOST': 'localhost',
        'NAME': 'sveetch_net',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'sveetch',
        'PASSWORD': '',
    }
}
