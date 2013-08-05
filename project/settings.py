# -*- coding: utf-8 -*-
#
# Django base settings for sveetch-net project.
#
# See "mods_enabled/" for "mods" settings

from os import listdir
from os.path import abspath, dirname, isfile, join

PROJECT_PATH = abspath(dirname(__file__))
VAR_PATH = join(PROJECT_PATH, '..', 'var')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('sveetch', 'sveetch@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': 'sveetchnet',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'django',
        'PASSWORD': 'dj4ng0',
    }
}

# Available cache backends
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'sveetchnet',
        'TIMEOUT': 60,
        'KEY_PREFIX': 'dev',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

"""
SMTP Settings to send Applications emails, configured for debug purpose only.

You will have to a launch a smtp daemon in parallel, like this :

    python -m smtpd -n -c DebuggingServer localhost:1025
"""
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_SUBJECT_PREFIX = '[sveetch-net Dev] '
SERVER_EMAIL = 'sveetch-net errors <your@mail.com>'
DEFAULT_FROM_EMAIL = 'sveetch-net <your@mail.com>'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gvo_-yn8&78jti6z16x!p^c-bal-l7u)k69ssr0kn^--q(1bc9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # admin
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LANGUAGES = [
    ('fr', u'Français'),
]


ALLOWED_HOSTS = ['*'] # FIXME Put here the domain names


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages')


#
# Mods system
#
def add_to_tuple(var, *args, **kw):
    """
    This utility method should be used to modify INSTALLED_APPS and the like.

    It features:

    - Avoid duplicates by checking whether the items are already there
    - Add many items at once
    - Allow to add the items before some other item, when order is important
      (by default it appends)

    Example:

        INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'foo', 'bar')
    """
    before = kw.get('before')

    var = list(var)
    for arg in args:
        if arg not in var:
            if before:
                var.insert(var.index(before), arg)
            else:
                var.append(arg)

    return tuple(var)


mods = join(PROJECT_PATH, 'mods_enabled')
mods = [ join(mods, x) for x in listdir(mods) ]
mods.sort()
for MOD_FILE in mods:
    mod = join(MOD_FILE, 'settings.py')
    if isfile(mod):
        execfile(mod)
