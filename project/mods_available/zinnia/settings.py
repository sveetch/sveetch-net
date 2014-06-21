# -*- coding: utf-8 -*-

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'south',
    'django.contrib.comments',
    'tagging',
    'mptt',
    'zinnia',
    'project.zinnia_ckeditor')


TEMPLATE_CONTEXT_PROCESSORS += (
    'zinnia.context_processors.version',)

ZINNIA_UPLOAD_TO = "zinnia/entries"
ZINNIA_PAGINATION = 10

ZINNIA_PING_EXTERNAL_URLS = False
ZINNIA_SAVE_PING_DIRECTORIES = False

# Extend Entry model to be able to specify the ckeditor widget to the 
# textareas in Entry admin
ZINNIA_WYSIWYG = None
ZINNIA_ENTRY_BASE_MODEL = 'project.zinnia_ckeditor.custom_entry_model.EntryWithCkeditor'
