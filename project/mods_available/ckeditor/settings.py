"""
Settings to enable the django-ckeditor
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'ckeditor')

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
            ['Image', 'Table', 'HorizontalRule'],
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
        'extraPlugins': 'blockquote,codemirror,div,justify,showblocks',
        
        # To enable showblocks on editor start without to use a button
        'startupOutlineBlocks': True,
        
        # Disable element filter to enable full HTML5, also this will let 
        # append any code, even bad syntax and malicious code, so be careful
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        # Lien pour activer "Explorer le serveur" au travers de django-filebrowser
        'filebrowserBrowseUrl': "/admin/filebrowser/browse?pop=3",
    },
}