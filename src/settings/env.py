from .custom_getenv import get_env

DEBUG = get_env('DEBUG', default=False, type=bool)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': get_env('DATABASE_ENGINE'),
        'NAME': get_env('DATABASE_NAME'),
        'USER': get_env('DATABASE_USER'),
        'PASSWORD': get_env('DATABASE_PASSWORD'),
        'HOST': get_env('DATABASE_HOST'),
        'PORT': get_env('DATABASE_PORT', default='5432'),
    }
}

BASE_URL = get_env('BASE_URL')

ENVIRONMENT = get_env('ENVIRONMENT')
