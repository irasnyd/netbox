import os
import random

def str2bool(s):
    return s.lower() in ('t', 'true', '1')

#########################
#                       #
#   Required settings   #
#                       #
#########################

# This is a list of valid fully-qualified domain names (FQDNs) for the NetBox server. NetBox will not permit write
# access to the server via any other hostnames. The first FQDN in the list will be treated as the preferred name.
#
# Example: ALLOWED_HOSTS = ['netbox.example.com', 'netbox.internal.local']
ALLOWED_HOSTS = ['*']

# PostgreSQL database configuration.
DATABASE = {
    'NAME': os.environ.get('DB_NAME', 'netbox'),
    'USER': os.environ.get('DB_USER', 'netbox'),
    'PASSWORD': os.environ.get('DB_PASS', 'netbox'),
    'HOST': os.environ.get('DB_HOST', 'localhost'),
    'PORT': os.environ.get('DB_PORT', '')
}

# This key is used for secure generation of random numbers and strings. It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters in length and contain a mix of letters, numbers, and
# symbols. NetBox will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY', '')


#########################
#                       #
#   Optional settings   #
#                       #
#########################

# Specify one or more name and email address tuples representing NetBox administrators. These people will be notified of
# application errors (assuming correct email settings are provided).
ADMINS = [
    # ['John Doe', 'jdoe@example.com'],
]

# Email settings
EMAIL = {
    'SERVER': os.environ.get('EMAIL_SERVER', 'localhost'),
    'PORT': int(os.environ.get('EMAIL_PORT', '25')),
    'USERNAME': os.environ.get('EMAIL_USERNAME', ''),
    'PASSWORD': os.environ.get('EMAIL_PASSWORD', ''),
    'TIMEOUT': int(os.environ.get('EMAIL_TIMEOUT', '10')),
    'FROM_EMAIL': os.environ.get('EMAIL_FROM', ''),
}

# Setting this to True will permit only authenticated users to access any part of NetBox. By default, anonymous users
# are permitted to access most data in NetBox (excluding secrets) but not make any changes.
LOGIN_REQUIRED = str2bool(os.environ.get('LOGIN_REQUIRED', 'False'))

# Setting this to True will display a "maintenance mode" banner at the top of every page.
MAINTENANCE_MODE = str2bool(os.environ.get('MAINTENANCE_MODE', 'False'))

# Credentials that NetBox will use to access live devices.
NETBOX_USERNAME = os.environ.get('DEVICE_USERNAME', '')
NETBOX_PASSWORD = os.environ.get('DEVICE_PASSWORD', '')

# Determine how many objects to display per page within a list. (Default: 50)
PAGINATE_COUNT = int(os.environ.get('PAGINATE_COUNT', '50'))

# Time zone (default: UTC)
TIME_ZONE = 'UTC'

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = 'N j, Y'
SHORT_DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'g:i a'
SHORT_TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'N j, Y g:i a'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'
