import sys
sys.path.append('/usr/src/app/')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from upload.models import Company, SicCode
import csv

def get_sic(code):
    parsed_code = code.split('-')[0].replace(' ', '')
    if parsed_code == '':
        return None
    return None if parsed_code.isalpha() else int(parsed_code)

with open('/usr/src/app/upload/basicdata/BasicCompanyDataAsOneFile-2020-05-01.csv') as f:
    reader = csv.reader(f)
    out = set()
    next(reader)
    for row in reader:
        try:
            c = Company.objects.get(pk=row[1])
        except Exception as e:
            print(e, row[1])
        sic_codes = [get_sic(i) for i in row[26:30] if get_sic(i)]
        try:
            sic_objs = [SicCode.objects.get(code=i) for i in sic_codes]
        except Exception as e:
            print(e, sic_codes, row[1])
            out.add(row[1])
        c.siccodes.add(*sic_objs)

print(out)
