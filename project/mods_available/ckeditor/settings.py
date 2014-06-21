"""
Settings to enable the django-ckeditor
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'ckeditor')

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = 'pillow'