import csv

import requests

from django.conf import settings
from django.core.cache import cache

from .models import Illustration


def fetch_csv(url=None):
    url = url or settings.DATA_URL
    try:
        r = cache.get_or_set('csv_file', requests.get(url), 60)
        return r.text.splitlines()
    except ConnectionError as e:
        return []

def load_csv():
    if settings.DEVEL:
        load_debug_csv()
        return
    try:
        f = fetch_csv()
        reader = csv.DictReader(f)
        for line in reader:
            populate_database(line)
    except ConnectionError:
        load_debug_csv()

def load_debug_csv(path=None):
    path = path or settings.DATA_PATH
    with open(path) as f:
        reader = csv.DictReader(f)
        for line in reader:
            populate_database(line)

def populate_database(data):
    image_url = data.pop('image')
    if image_url:
        obj, created = Illustration.objects.update_or_create(
            image_url=image_url, defaults=data)
    elif data['title']:
        title = data.pop('title')
        obj, created = Illustration.objects.update_or_create(
            title=title, defaults=data)
    else:
        pass  # No object creation/update
