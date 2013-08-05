"""
Settings to enable the django-debug-toolbar
"""
# Must match the IP adress you will use to access to the instance
INTERNAL_IPS = ()

# Options 
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PANELS = (
    #'debug_toolbar_user_panel.panels.UserPanel',
    #'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    #'debug_toolbar.panels.signals.SignalDebugPanel',
    #'debug_toolbar.panels.logger.LoggingPanel',
)

MIDDLEWARE_CLASSES = add_to_tuple(MIDDLEWARE_CLASSES, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'debug_toolbar')
