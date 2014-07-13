# -*- coding: utf-8 -*-
from project.zinnia_ckeditor.views import EditorTemplatesListView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^editor_site_templates.js$', EditorTemplatesListView.as_view(), name="ckeditor-editor-site-templates"),
)
