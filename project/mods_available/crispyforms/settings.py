# -*- coding: utf-8 -*-
"""
Settings to enable crispy-form-foundation
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'crispy_forms', 'crispy_forms_foundation')

CRISPY_FAIL_SILENTLY = not DEBUG

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'foundation'
