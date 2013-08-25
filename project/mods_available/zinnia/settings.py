# -*- coding: utf-8 -*-

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'south',
    'django.contrib.comments',
    'tagging',
    'mptt',
    'zinnia')


TEMPLATE_CONTEXT_PROCESSORS += (
    'zinnia.context_processors.version',)

ZINNIA_UPLOAD_TO = "zinnia/entries"
ZINNIA_PAGINATION = 3

#ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia.spam_checker.backends.automattic',)
#AKISMET_SECRET_API_KEY = '5e91b4dd3dcd'

ZINNIA_PING_EXTERNAL_URLS = False
ZINNIA_SAVE_PING_DIRECTORIES = False