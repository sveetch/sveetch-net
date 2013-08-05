# -*- coding: utf-8 -*-
"""
Map your djangocodemirror urls
"""
urlpatterns = patterns('',
    (r'^djangocodemirror-sample/', include('djangocodemirror.urls')),
) + urlpatterns
