#!/usr/local/bin/python

import sys
sys.path.append('/usr/src/app/')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from upload.models import Category, SicCode
import csv

with open('/usr/src/app/upload/siccodes/siccodes.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        s = SicCode()
        s.code = row[0]
        s.description = row[1]
        s.save()
        titles = [i for i in row[2:8] if i]
        try:
            cats = [Category.objects.get(title=i) for i in titles]
        except Exception as e:
            print(e, titles)
            continue
        s.category.add(*cats)
