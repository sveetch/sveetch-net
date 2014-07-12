# -*- coding: utf-8 -*-
import os

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'filebrowser',
                              before="ckeditor")

FILEBROWSER_VERSIONS_BASEDIR = '_uploads_versions'

FILEBROWSER_MAX_UPLOAD_SIZE = 20*1024*1024 # 20 Mb

FILEBROWSER_NORMALIZE_FILENAME = True