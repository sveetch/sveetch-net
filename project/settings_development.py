# Import
from project.settings import *

DEBUG = TEMPLATE_DEBUG = True
ASSETS_DEBUG = True
INTERNAL_IPS = ('192.168.0.112',)

# SMTP Settings to send Applications emails, configured for debug purpose only
# $> python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_SUBJECT_PREFIX = '[sveetch-net Dev] '
SERVER_EMAIL = 'sveetch-net errors <sveetch@gmail.com>'
DEFAULT_FROM_EMAIL = 'sveetch-net <sveetch@gmail.com>'
