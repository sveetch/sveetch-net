# -*- coding: utf-8 -*-
"""
Map your djangocodemirror urls
"""
urlpatterns = patterns('',
    (r'^crispy-forms-foundation/', include('crispy_forms_foundation.urls')),
) + urlpatterns
