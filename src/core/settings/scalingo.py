from pathlib import Path

import dj_database_url
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa
from .base import INSTALLED_APPS, TEMPLATES


# Sometime, we want to load Scalingo environment from a dotenv file.
# This is specially useful when testing Scalingo setup from a local dev
if Path('.env.scalingo').exists():
    environ.Env.read_env('.env.scalingo')

env = environ.Env()

ENV_NAME = env('ENV_NAME')

SETTINGS_DIR = Path(__file__).parent
CORE_APP_DIR = SETTINGS_DIR.parent
DJANGO_ROOT = CORE_APP_DIR.parent

SECRET_KEY = env('SECRET_KEY')

DATABASES = {'default': dj_database_url.config()}

DEBUG = env.bool('DEBUG', False)

sentry_sdk.init(
    dsn=env.str('SENTRY_URL'),
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)

COMPRESS_OFFLINE = env.bool('COMPRESS_OFFLINE', default=False)
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', default=True)

NODE_MODULES_PATH = Path(DJANGO_ROOT, 'node_modules')

SASS_PATH = 'make css'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', '{} include={} infile={{infile}} outfile={{outfile}}'.format(
        SASS_PATH, NODE_MODULES_PATH)),
)

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [
    Path(DJANGO_ROOT, 'static'),
    Path(DJANGO_ROOT, 'node_modules'),
]

TEMPLATES = TEMPLATES.copy()
TEMPLATES[0]['DIRS'] = [Path(DJANGO_ROOT, 'templates')]

LOCALE_PATHS = [
    Path(DJANGO_ROOT, 'locales'),
]

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='memory://')
CELERY_TASK_ALWAYS_EAGER = env('CELERY_TASK_ALWAYS_EAGER', default=True)
CELERY_TASK_EAGER_PROPAGATES = env('CELERY_TASK_EAGER_PROPAGATES', default=True)

env_allowed_hosts = []
try:
    env_allowed_hosts = env('ALLOWED_HOSTS', default='').split(",")
except KeyError:
    pass

INTERNAL_IPS = env.list('INTERNAL_IPS', default=['127.0.0.1'])

ALLOWED_HOSTS = ["localhost"] + env_allowed_hosts

MAILING_LIST_URL = env('MAILING_LIST_URL', default='')

EMAIL_BACKEND = env('EMAIL_BACKEND')

EMAIL_WHITELIST = env.list('EMAIL_WHITELIST', [])

# Sendinblue api and settings
SIB_API_KEY = env('SIB_API_KEY')
SIB_LIST_ID = env.int('SIB_LIST_ID')
ANYMAIL = {
    'SENDINBLUE_API_KEY': SIB_API_KEY,
}
SIB_WELCOME_EMAIL_TEMPLATE_ID = env.int('SIB_WELCOME_EMAIL_TEMPLATE_ID', 0)
SIB_WELCOME_EMAIL_ENABLED = env.bool('SIB_WELCOME_EMAIL_ENABLED', False)
SIB_PUBLICATION_EMAIL_TEMPLATE_ID = env.int('SIB_PUBLICATION_EMAIL_TEMPLATE_ID', 0)
SIB_PUBLICATION_EMAIL_ENABLED = env.bool('SIB_PUBLICATION_EMAIL_ENABLED', False)

# File storage settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_DEFAULT_ACL = 'public-read'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Piwik goal tracking ids
GOAL_REGISTER_ID = env.int('GOAL_REGISTER_ID', 1)
GOAL_FIRST_LOGIN_ID = env.int('GOAL_FIRST_LOGIN_ID', 2)
