# -*- coding: utf-8 -*-
"""
Map your djangotribune urls
"""
urlpatterns += patterns('',
    url(r'^tribune/', include('djangotribune.urls')),
)
