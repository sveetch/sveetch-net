# -*- coding: utf-8 -*-
"""
Settings to enable autobreadcrumbs
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'autobreadcrumbs')

TEMPLATE_CONTEXT_PROCESSORS = add_to_tuple(TEMPLATE_CONTEXT_PROCESSORS, 'autobreadcrumbs.context_processors.AutoBreadcrumbsContext')
