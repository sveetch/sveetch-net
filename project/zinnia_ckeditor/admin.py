from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ckeditor.widgets import CKEditorWidget

from zinnia.models.entry import Entry
from zinnia.admin.entry import EntryAdmin

class EntryWithCkeditor(EntryAdmin):
    """
    Customize entry admin to use ckeditor widget
    
    We should try something more stable and clean than override all TextField fields
    """
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='zinnia')},
    }

# Unregister the default EntryAdmin
# then register the EntryWithCkeditor class
admin.site.unregister(Entry)
admin.site.register(Entry, EntryWithCkeditor)