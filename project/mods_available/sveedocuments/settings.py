# -*- coding: utf-8 -*-
"""
Settings to enable sveedocuments
"""
from django.utils.translation import ugettext_lazy

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'rstview', 'mptt', 'sveedocuments')
TEMPLATE_CONTEXT_PROCESSORS = add_to_tuple(TEMPLATE_CONTEXT_PROCESSORS, 'sveedocuments.context_processors.SveedocumentsContext')

# The docutils writer to use, can be html4 or html5, html5 writer is internal code of 
# sveedocuments
RSTVIEW_PARSER_WRITER = "html5"

# Add some addtional templates
# NOTE: Usage of ugettext_lazy in settings should be prohibited
DOCUMENTS_PAGE_TEMPLATES = {
    'fixed_1_cols': ('sveedocuments/page_details/fixed_1_cols.html', ugettext_lazy('Fixed layout with one column')),
    'elastic_2_cols': ('sveedocuments/page_details/elastic_2_cols.html', ugettext_lazy('Elastic layout with two column')),
}
# Custom cache keys to remove with clearcache command option
DOCUMENTS_CACHE_KEYS_TO_CLEAN = ["applications_toc_on_homepage"]

# Forbidden words for slug values in documents to avoid clashes in urls
DOCUMENTS_PAGE_RESERVED_SLUGS = (
    'add', 'admin', 'board', 'preview', 'inserts', 'documents-help', 'sitemap', # for sveedocuments
    'djangocodemirror-sample', # for djangocodemirror sample
    'accounts', 'captcha', # for sveeaccounts
    'tribune', # for djangotribune
)

# Cookie name used to store and retreive user settings for editor
DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME = "djangocodemirror_user_settings"

# Additional Django-CodeMirror settings for sveedocuments
CODEMIRROR_SETTINGS = {
    'sveetchies-documents-page': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'preview_url': ('documents-preview',),
        'quicksave_url': ('documents-page-quicksave',),
        'quicksave_datas': 'DJANGOCODEMIRROR_OBJECT',
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
        'settings_cookie': DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
        'help_link': ('documents-help',),
        'settings_url': ('documents-editor-settings', [], {}),
    },
    'sveetchies-documents-insert': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'preview_url': ('documents-preview',),
        'quicksave_url': ('documents-insert-quicksave',),
        'quicksave_datas': 'DJANGOCODEMIRROR_OBJECT',
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
        'settings_cookie': DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
        'help_link': ('documents-help',),
        'settings_url': ('documents-editor-settings', [], {}),
    },
}
