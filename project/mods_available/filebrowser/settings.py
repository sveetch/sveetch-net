# -*- coding: utf-8 -*-
import os

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'filebrowser',
                              before="ckeditor")

## Needed for compatibility with filebrowser_no_grapelli that use
## ADMIN_MEDIA_PREFIX when tinymce is not installed, sadly this raise a
## warning by Django >= 1.5
#ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, "admin/")

FILEBROWSER_VERSIONS_BASEDIR = '_uploads_versions'

FILEBROWSER_MAX_UPLOAD_SIZE = 20*1024*1024 # 20 Mb

FILEBROWSER_NORMALIZE_FILENAME = True