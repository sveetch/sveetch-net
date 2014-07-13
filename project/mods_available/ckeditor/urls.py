urlpatterns = patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^ckeditor/', include('project.zinnia_ckeditor.urls')),
    ) + urlpatterns
