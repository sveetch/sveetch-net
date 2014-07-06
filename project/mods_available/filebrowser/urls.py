# -*- coding: utf-8 -*-
from filebrowser.sites import site

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    ) + urlpatterns
