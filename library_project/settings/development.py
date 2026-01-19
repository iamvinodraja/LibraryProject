# """
# Development server settings.
# """
# from .base import *
# import os

# DEBUG = True

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'library_db'),
#         'USER': os.getenv('DB_USER', 'postgres'),
#         'PASSWORD': os.getenv('DB_PASSWORD', ''),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }
"""
Development server settings.
"""
from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'library_db'),
        'USER': os.getenv('DB_USER', 'library_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
