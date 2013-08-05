# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    ) + urlpatterns
