#!/usr/local/bin/python3

import sys
sys.path.append('/usr/src/app/')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from upload.models import Category
import csv

with open('/usr/src/app/upload/categories/cat_list.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        c = Category()
        c.title = row[0]
        c.description = row[1]
        c.save()

