# -*- coding: utf-8 -*-
"""
Views to customize CKEditor

These views are for admin staff only, we don't want to expose them.
"""
import os, json

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from django.template.base import TemplateDoesNotExist
from django.template.loader import find_template_loader

class StaffuserRequiredMixin(object):
    """
    Mixin allows you to require a user with `is_staff` set to True.
        
    Taken from django-braces
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:  # If the request's user is not staff,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response
            else:
                return redirect_to_login(request.get_full_path(),
                                         self.login_url,
                                         self.redirect_field_name)

        return super(StaffuserRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class EditorTemplatesListView(StaffuserRequiredMixin, View):
    """
    Recursively list all HTML file in settings.CKEDITOR_EDITOR_TEMPLATES_PATH 
    that didn't start with "_" and return the list in a Javascript file :
    
        // Register a templates definition set named "default".
        CKEDITOR.addTemplates( 'default', {
            // The name of sub folder which hold the shortcut preview images of the
            // templates.
            imagesPath: '/static/ckeditor/editor-site-templates/',

            // The templates definitions.
            templates: [
                {
                    title: 'Grid row',
                    image: 'grid_row.gif',
                    description: 'Sample',
                    html: '<div class="row"></div>'
                }
            ]
        }
    
    This will use the filesystem and apps template loaders to find a JSON manifest and 
    find templates from his directory. If a finded template file is not defined in the 
    manifest it will be ignored.
    
    On the root of the settings.CKEDITOR_EDITOR_TEMPLATES_PATH directory, 
    must resides a "manifest.json" file that contain a map to your content templates to 
    declare their optionnal title and description. When a content template has no 
    declared title it take his relative path as title, and the default description is 
    empty.
    
    Your "manifest.json" file should look like :
    
        {
            "foo.html": {
                "title": "Dummy",
                "image": "grid_row.gif",
                "description": "Dummy template for testing"
            }
        }
        
    The template HTML is taken from the template filename given at the key name.
    
    Take care to make valid JSON, else this will raise exception. Also note that content 
    templates are indexed on their filename.
    """
    def get(self, request, *args, **kwargs):
        imagespath = os.path.join(settings.STATIC_URL, settings.CKEDITOR_EDITOR_TEMPLATES_IMAGES_PATH)
        return HttpResponse(
                    settings.CKEDITOR_EDITOR_JS_TEMPLATE.format(imagespath=imagespath, json_list=json.dumps(self.get_templates(), indent=4)),
                    content_type="application/javascript"
                )
    
    def get_manifest(self):
        """
        Find the absolute path to the content templates manifest JSON file using 
        filesystem and app template loaders
        
        Return a tuple containing two items:
        * a dict from the manifest if finded, else an empty dict
        * if manifest is finded, an absolute path to use to find content templates, else None
        """
        manifest_filepath = os.path.join(settings.CKEDITOR_EDITOR_TEMPLATES_PATH, settings.CKEDITOR_EDITOR_TEMPLATES_MANIFEST_FILENAME)
        for item in settings.TEMPLATE_LOADERS:
            current_loader = find_template_loader(item)
            if current_loader.is_usable:
                try:
                    template, origin = current_loader.load_template_source(manifest_filepath)
                except TemplateDoesNotExist:
                    pass
                else:
                    if origin:
                        return json.load(open(origin, 'r')), os.path.dirname(origin)
        
        return {}, None
    
    def get_templates(self):
        manifest, paths = {}, []
        # Default entrie dict to copy for a new content template to have 
        # default values
        TPL_OBJ = {
            'title': 'Dummy title',
            'image': '',
            'description': '',
            'html': 'Empty'
        }
        
        manifest_file, templates_dir = self.get_manifest()
        
        if templates_dir:
            manifest.update(manifest_file)
            
            # Find templates in the manifest directory
            for root, dirs, files in os.walk(templates_dir):
                
                for name in sorted(files):
                    # Get only HTML files, excludes thoses ones that starts 
                    # with a dot or an underscore
                    if not name.startswith('.') and not name.startswith('_') and name.endswith('.html'):
                        item_obj = TPL_OBJ.copy()
                        absolute = os.path.join(root, name)
                        relative = os.path.relpath(absolute, templates_dir)
                        # Default content
                        item_obj['title'] = name
                        # Get the HTML content
                        fp = open(absolute, "r")
                        item_obj['html'] = fp.read()
                        fp.close()
                        # If the entry is defined in the manifest
                        if relative in manifest:
                            item_obj['title'] = manifest[relative].get('title') or item_obj['title']
                            item_obj['description'] = manifest[relative].get('description') or item_obj['description']
                            item_obj['image'] = manifest[relative].get('image') or item_obj['image']
                            
                            paths.append(item_obj)
        
        return paths
        