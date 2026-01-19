"""
Loads the appropriate settings based on DJANGO_ENVIRONMENT.
Default: local
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')

ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'local')

if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'development':
    from .development import *
else:
    from .local import *
