from settings import *
from settings import BASE_DIR
import os

# Retrieve environment variables
WEBSITE_HOSTNAME = os.environ.get('WEBSITE_HOSTNAME', '')

# Set allowed hosts and CSRF trusted origins
ALLOWED_HOSTS = [WEBSITE_HOSTNAME] if WEBSITE_HOSTNAME else []
CSRF_TRUSTED_ORIGINS = [f'https://{WEBSITE_HOSTNAME}'] if WEBSITE_HOSTNAME else []

# Debug mode
DEBUG = False

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# Static files settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Parse connection string
CONNECTION = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING', '')
CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')} if CONNECTION else {}

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': CONNECTION_STR.get('dbname', ''),
        'HOST': CONNECTION_STR.get('host', ''),
        'USER': CONNECTION_STR.get('user', ''),
        'PASSWORD': CONNECTION_STR.get('password', ''),
    }
}
