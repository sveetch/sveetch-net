# -*- coding: utf-8 -*-
"""
Settings to enable sveeaccounts
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'registration', 'captcha', 'sveeaccounts')

"""
Settings for django-registration
"""
# Default URL to redirect to just after successful login
LOGIN_REDIRECT_URL = "/"
# Days until a waiting registration is closed
ACCOUNT_ACTIVATION_DAYS = 3
