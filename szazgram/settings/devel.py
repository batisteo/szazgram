from .base import *

# DEVEL = True
DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATA_PATH = 'test_application_data.csv'
