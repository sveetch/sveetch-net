"""
Settings to enable the django-ckeditor
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'ckeditor', 'project.zinnia_ckeditor')

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'zinnia': {
        # Reorganize/remove/add buttons
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike'],
            ['Link', 'Unlink'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['Blockquote', 'CreateDiv'],
            ['Image', 'Table', 'Templates'],
            ['Undo', 'Redo'],
            ['Source'],
            ['Maximize'],
        ],
        
        # Wider editor
        'height': 400,
        'width': 980,
        
        # Justifiy classes with Foundation naming
        'justifyClasses': [ 'text-left', 'text-center', 'text-right', 'AlignJustify' ],
        
        # Enable some plugins
        'extraPlugins': 'blockquote,codemirror,div,justify,showblocks,image2,templates',
        
        # To enable showblocks on editor start without to use a button
        'startupOutlineBlocks': True,
        
        # Disable element filter to enable full HTML5, also this will let 
        # append any code, even bad syntax and malicious code, so be careful
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        
        # Link to use for the link "Browse server"
        'filebrowserBrowseUrl': "/admin/filebrowser/browse?pop=3",
        
        # Content templates option to not overwrite the whole content when using a template
        'templates_replaceContent': False,
        # Script URL to load JSON manifest for content templates
        'templates_files': [
            '/ckeditor/editor_site_templates.js'
        ],
    },
}

# Path (relative to a project template dir) for ckeditor "content templates" directory
CKEDITOR_EDITOR_TEMPLATES_PATH = "ckeditor/editor-site-templates/"
# Path (relative to the static dir) for ckeditor "content templates" image thumbs directory
CKEDITOR_EDITOR_TEMPLATES_IMAGES_PATH = "ckeditor/editor-site-templates/"
# Filename path (relative to CKEDITOR_EDITOR_TEMPLATES_PATH) to search for template manifest
CKEDITOR_EDITOR_TEMPLATES_MANIFEST_FILENAME = "manifest.json"
# Template string to use to declare content templates
CKEDITOR_EDITOR_JS_TEMPLATE = u"""CKEDITOR.addTemplates( 'default', {{imagesPath:"{imagespath}", templates: {json_list}}});"""
