from .base import *

# DEVEL = True
DEBUG = True

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache_szazgram',
    }
}

DATA_PATH = 'test_application_data.csv'
