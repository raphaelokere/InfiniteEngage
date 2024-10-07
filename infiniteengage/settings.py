import os
from pathlib import Path
import dj_database_url  # For database configuration in production

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')  # Use environment variable for secret key
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'  # Ensures DEBUG is True by default in development, False in production

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost 127.0.0.1 infiniteengage-ccegc6dnhzahc2fb.eastus2-01.azurewebsites.net').split()

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Your main app
]

CSRF_TRUSTED_ORIGINS = ['https://infiniteengage-ccegc6dnhzahc2fb.eastus2-01.azurewebsites.net']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.azuread.AzureADOAuth2',
    'django.contrib.auth.backends.ModelBackend',  # Keep the default backend for admin login
)

SOCIAL_AUTH_AZUREAD_OAUTH2_KEY = os.getenv('AZURE_CLIENT_ID')  # Client ID from Azure AD
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET = os.getenv('AZURE_CLIENT_SECRET')  # Client Secret from Azure AD
SOCIAL_AUTH_AZUREAD_OAUTH2_TENANT_ID = os.getenv('AZURE_TENANT_ID')  # Tenant ID from Azure AD

# Redirect after login
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# URL Configuration
ROOT_URLCONF = 'infiniteengage.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI and ASGI Configuration
WSGI_APPLICATION = 'infiniteengage.wsgi.application'

# Database configuration
# Use SQLite for development and PostgreSQL for production (Azure)
if os.environ.get('DJANGO_ENV') == 'production':
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL')
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Where static files will be collected in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
if os.environ.get('DJANGO_ENV') == 'production':
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# For handling Azure Blob Storage for static and media files (optional for production)
if os.environ.get('USE_AZURE_STORAGE') == 'True':
    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')
    AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER')
    
    STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'  # Optional if you want static files in Azure
