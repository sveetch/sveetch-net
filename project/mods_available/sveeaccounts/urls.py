# -*- coding: utf-8 -*-
"""
Map your sveeaccounts urls
"""
urlpatterns = patterns('',
    (r'^accounts/', include('sveeaccounts.urls')),
) + urlpatterns
