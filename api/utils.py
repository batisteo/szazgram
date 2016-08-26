import csv

import requests
from requests.exceptions import ConnectionError, Timeout

from django.conf import settings
from django.core.files import File
from django.core.cache import cache

from .models import Illustration


def _fetch_csv(url):
    try:
        r = requests.get(url, timeout=5)
        return r.text.splitlines()
    except (ConnectionError, Timeout) as e:
        print('Failed to load the CSV file from Internet')
        return []

def fetch_csv(url=None):
    url = url or settings.DATA_URL
    if cache.get('csv_file'):
        print('in cache :)')
        return cache.get('csv_file')
    print('fetching from web...')
    csv_file = _fetch_csv(url)
    if csv_file:
        print('caching...')
        cache.set('csv_file', csv_file, 60)
        print('done')
    return csv_file

def load_csv():
    if settings.DEVEL:
        load_debug_csv()
        return
    f = fetch_csv()
    reader = csv.DictReader(f)
    for line in reader:
        populate_database(line)

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
        if created:
            # Try to download a pic, resize and put it in 'image' field
            obj.save_image(url)
    elif data['title']:
        title = data.pop('title')
        obj, created = Illustration.objects.update_or_create(
            title=title, defaults=data)
    else:
        pass  # No object creation/update
