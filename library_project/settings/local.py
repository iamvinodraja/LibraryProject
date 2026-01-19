"""
Local development settings.
"""
from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Choose database based on DB_ENGINE in .env
db_engine = os.getenv('DB_ENGINE', 'sqlite')

if db_engine == 'postgresql':
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
else:
    # Default to SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }