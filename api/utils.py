import csv

import requests

from .models import Illustration


def fetch_csv(url):
    r = requests.get(url)
    return r.text.splitlines()

def get_offline_csv(path):
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
