#!/usr/local/bin/python3

import sys
sys.path.append('/usr/src/app/')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from upload.models import Company
import csv
from datetime import datetime

def get_date(date):
    try:
        date = [int(i) for i in date.split('/')]
        return datetime(date[2],date[1],date[0])
    except:
        return None

def get_num(num):
    return None if num == '' else int(num)

def get_sic(code):
    parsed_code = code.split('-')[0].replace(' ', '')
    return None if parsed_code.isalpha() else int(parsed_code)

batch_size = 100
objs = []
with open('/usr/src/app/upload/basicdata/BasicCompanyDataAsOneFile-2020-05-01.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        objs.append(Company(
        companyname = row[0],
        companynumber = row[1],
        regaddress_careof = row[2] ,
        regaddress_pobox = row[3],
        regaddress_addressline1 = row[4] ,
        regaddress_addressline2 = row[5] ,
        regaddress_posttown = row[6] ,
        regaddress_county = row[7] ,
        regaddress_country = row[8] ,
        regaddress_postcode = row[9] ,
        companycategory = row[10] ,
        companystatus = row[11] ,
        countryoforigin = row[12] ,
        dissolutiondate = get_date(row[13]),
        incorporationdate = get_date(row[14]),
        accounts_accountrefday = get_num(row[15]),
        accounts_accountrefmonth = get_num(row[16]),
        accounts_nextduedate = get_date(row[17]),
        accounts_lastmadeupdate = get_date(row[18]),
        accounts_accountcategory = row[19],
        returns_nextduedate = get_date(row[20]),
        returns_lastmadeupdate = get_date(row[21]),
        mortgages_nummortcharges = row[22],
        mortgages_nummortoutstanding = row[23],
        mortgages_nummortpartsatisfied = row[24],
        mortgages_nummortsatisfied = row[25],
#        siccode_sictext_1 = SicCode.object.get(pk=get_sic(row[26])),
#        siccode_sictext_2 = SicCode.object.get(pk=get_sic(row[27])),
#        siccode_sictext_3 = SicCode.object.get(pk=get_sic(row[28])),
#        siccode_sictext_4 = SicCode.object.get(pk=get_sic(row[29])),
        limitedpartnerships_numgenpartners = row[30],
        limitedpartnerships_numlimpartners = row[31],
        url = row[32],
        previousname_1_condate = get_date(row[33]),
        previousname_1_companyname = row[34],
        previousname_2_condate = get_date(row[35]),
        previousname_2_companyname = row[36],
        previousname_3_condate = get_date(row[37]),
        previousname_3_companyname = row[38],
        previousname_4_condate = get_date(row[39]),
        previousname_4_companyname = row[40],
        previousname_5_condate = get_date(row[41]),
        previousname_5_companyname = row[42],
        previousname_6_condate = get_date(row[43]),
        previousname_6_companyname = row[44],
        previousname_7_condate = get_date(row[45]),
        previousname_7_companyname = row[46],
        previousname_8_condate = get_date(row[47]),
        previousname_8_companyname = row[48],
        previousname_9_condate = get_date(row[49]),
        previousname_9_companyname = row[50],
        previousname_10_condate = get_date(row[51]),
        previousname_10_companyname = row[52],
        confstmtnextduedate = get_date(row[53]),
        confstmtlastmadeupdate = get_date(row[54]),
        ))
        if len(objs) > batch_size:
            Company.objects.bulk_create(objs, ignore_conflicts=True)
            objs = []
    Company.objects.bulk_create(objs, ignore_conflicts=True)

