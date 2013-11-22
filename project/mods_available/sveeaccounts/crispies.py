# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, Row, Column, ButtonHolder, Submit

def LoginHelper():
    """
    Simple helper for the login form
    """
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Row(
            Column(
                'username',
                'password',
                css_class='twelve'
            ),
        ),
    )
    
    return helper

def PasswordResetFormHelper():
    """
    Simple helper for the password reset form
    """
    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column(
                'email',
                css_class='twelve'
            ),
        ),
        Row(
            Column(
                Submit('submit', _('Submit')),
                css_class='twelve text-right'
            ),
        )
    )
    
    return helper

def PasswordResetChangeFormHelper():
    """
    Simple helper for the login form
    """
    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column(
                'new_password1',
                'new_password2',
                css_class='twelve'
            ),
        ),
        Row(
            Column(
                Submit('submit', _('Submit')),
                css_class='twelve text-right'
            ),
        )
    )
    
    return helper

def RegistrationFormHelper():
    """
    Helper for the user registration form
    """
    helper = FormHelper()
    helper.form_action = '.'
    helper.layout = Layout(
        Row(
            Column(
                'email',
                'username',
                css_class='twelve'
            ),
        ),
        Row(
            Column(
                'password1',
                css_class='six'
            ),
            Column(
                'password2',
                css_class='six'
            ),
        ),
        Row(
            Column(
                'captcha',
                css_class='twelve'
            ),
        ),
        Row(
            Column(
                ButtonHolder( Submit('submit', _('Submit')), css_class="text-right" ),
                css_class='twelve'
            ),
        )
    )
    
    return helper

def UserFormHelper():
    """
    Helper for the user edit form
    """
    helper = FormHelper()
    helper.form_action = '.'
    helper.layout = Layout(
        Fieldset(
            _('Identity'),
            Row(
                Column(
                    'email',
                    css_class='twelve'
                ),
            ),
            Row(
                Column(
                    'first_name',
                    css_class='six'
                ),
                Column(
                    'last_name',
                    css_class='six'
                ),
            ),
        ),
        Fieldset(
            _('Password'),
            Row(
                Column(
                    'new_password1',
                    css_class='twelve'
                ),
                Column(
                    'new_password2',
                    css_class='twelve'
                ),
            ),
        ),
        Row(
            Column(
                ButtonHolder( Submit('submit', _('Submit')), css_class="text-right" ),
                css_class='twelve'
            ),
        )
    )
    
    return helper
