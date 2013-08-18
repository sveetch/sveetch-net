# -*- coding: utf-8 -*-
from zinnia.views.archives import EntryIndex

urlpatterns = patterns('',
    url(r'^$', EntryIndex.as_view(), name='homepage'),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    ) + urlpatterns
