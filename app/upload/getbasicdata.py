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


with open('/usr/src/app/upload/BasicCompanyDataAsOneFile-2020-05-01.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        c = Company()
        c.companyname = row[0]
        c.companynumber = row[1]
        c.regaddress_careof = row[2] 
        c.regaddress_pobox = row[3]
        c.regaddress_addressline1 = row[4] 
        c.regaddress_addressline2 = row[5] 
        c.regaddress_posttown = row[6] 
        c.regaddress_county = row[7] 
        c.regaddress_country = row[8] 
        c.regaddress_postcode = row[9] 
        c.companycategory = row[10] 
        c.companystatus = row[11] 
        c.countryoforigin = row[12] 
        c.dissolutiondate = get_date(row[13])
        c.incorporationdate = get_date(row[14])
        c.accounts_accountrefday = get_num(row[15])
        c.accounts_accountrefmonth = get_num(row[16])
        c.accounts_nextduedate = get_date(row[17])
        c.accounts_lastmadeupdate = get_date(row[18])
        c.accounts_accountcategory = row[19]
        c.returns_nextduedate = get_date(row[20])
        c.returns_lastmadeupdate = get_date(row[21])
        c.mortgages_nummortcharges = row[22]
        c.mortgages_nummortoutstanding = row[23]
        c.mortgages_nummortpartsatisfied = row[24]
        c.mortgages_nummortsatisfied = row[25]
        c.siccode_sictext_1 = row[26] 
        c.siccode_sictext_2 = row[27] 
        c.siccode_sictext_3 = row[28] 
        c.siccode_sictext_4 = row[29]
        c.limitedpartnerships_numgenpartners = row[30]
        c.limitedpartnerships_numlimpartners = row[31]
        c.url = row[32]
        c.previousname_1_condate = get_date(row[33])
        c.previousname_1_companyname = row[34]
        c.previousname_2_condate = get_date(row[35])
        c.previousname_2_companyname = row[36]
        c.previousname_3_condate = get_date(row[37])
        c.previousname_3_companyname = row[38]
        c.previousname_4_condate = get_date(row[39])
        c.previousname_4_companyname = row[40]
        c.previousname_5_condate = get_date(row[41])
        c.previousname_5_companyname = row[42]
        c.previousname_6_condate = get_date(row[43])
        c.previousname_6_companyname = row[44]
        c.previousname_7_condate = get_date(row[45])
        c.previousname_7_companyname = row[46]
        c.previousname_8_condate = get_date(row[47])
        c.previousname_8_companyname = row[48]
        c.previousname_9_condate = get_date(row[49])
        c.previousname_9_companyname = row[50]
        c.previousname_10_condate = get_date(row[51])
        c.previousname_10_companyname = row[52]
        c.confstmtnextduedate = get_date(row[53])
        c.confstmtlastmadeupdate = get_date(row[54])
        c.save()

