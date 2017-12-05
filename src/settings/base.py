import os
import sys

# ~~~~~~~~~~~~ Directory Paths ~~~~~~~~~~~~~~~

BASE_DIRECTORY = os.path.dirname(os.path.dirname(__file__))  # src/ directory

sys.path.insert(1, os.path.join(BASE_DIRECTORY, 'apps'))

LOG_DIRECTORY = os.path.join(os.path.dirname(BASE_DIRECTORY), 'logs')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SECRET_FILE = os.path.normpath(os.path.join(BASE_DIRECTORY, 'SECRET.key'))

ADMINS = (
    ('Zeeshan Asgar', 'asgarzeeshan@gmail.com'),
)

MANAGERS = ADMINS

SESSION_COOKIE_AGE = 31536000

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'django_fsm',
    'fsm_admin',
    'flow.apps.FlowConfig',

]

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += DEFAULT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'src.urls'

WSGI_APPLICATION = 'src.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_PATH = os.path.join(BASE_DIRECTORY, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIRECTORY, 'media')
MEDIA_URL = '/media/'
PDF_ROOT = os.path.join(STATIC_PATH, 'pdf')

STATIC_ROOT = os.path.join(BASE_DIRECTORY, "..", "static")
STATICFILES_DIRS = (
    STATIC_PATH,
)

TEMPLATE_PATH = os.path.join(BASE_DIRECTORY, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'application_logs': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIRECTORY, 'applications.log'),
            'formatter': 'standard',
        },
        'debug_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIRECTORY, 'project.log'),
            'formatter': 'standard',
        }
    },
    'root': {
        'handlers': ['console', 'debug_log_file', 'application_logs'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        from django.utils.crypto import get_random_string

        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
        SECRET_KEY = get_random_string(50, chars)
        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Unable to open %s' % SECRET_FILE)

from .env import *
