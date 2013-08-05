# -*- coding: utf-8 -*-
"""
Urls map for captcha mod
"""
urlpatterns = patterns('',
    (r'^captcha/', include('captcha.urls')),
) + urlpatterns
