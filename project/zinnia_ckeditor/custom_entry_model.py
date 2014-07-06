"""
Must not be in models.py to avoid a clash with zinnia models
"""
from django.utils.translation import ugettext_lazy as _

from zinnia.models.entry import EntryAbstractClass

from ckeditor.fields import RichTextField

class EntryWithCkeditor(EntryAbstractClass):
    class Meta(EntryAbstractClass.Meta):
        abstract = True
