# -*- coding: utf-8 -*-
"""
Settings to enable sveeaccounts
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'registration', 'captcha', 'sveeaccounts', before='django.contrib.auth')

# Custom helpers for the "accounts" forms
REGISTRATION_FORM_HELPER = "project.mods_available.sveeaccounts.crispies.RegistrationFormHelper"
REGISTRATION_LOGIN_HELPER = "project.mods_available.sveeaccounts.crispies.LoginHelper"
REGISTRATION_USER_EDIT_HELPER = "project.mods_available.sveeaccounts.crispies.UserFormHelper"
REGISTRATION_PASSWORD_RESET_HELPER = "project.mods_available.sveeaccounts.crispies.PasswordResetFormHelper"
REGISTRATION_PASSWORD_RESET_CHANGE_HELPER = "project.mods_available.sveeaccounts.crispies.PasswordResetChangeFormHelper"

"""
Settings for django-registration
"""
# Default URL to redirect to just after successful login
LOGIN_REDIRECT_URL = "/"
# Days until a waiting registration is closed
ACCOUNT_ACTIVATION_DAYS = 3
