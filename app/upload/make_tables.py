import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from .models import Accounts
from .header_lookup import TITLE_LOOKUP


def make_tables(ttype='basic', sortby='companyname', sortdirection='increasing', items=1000):
    query_set = Accounts.objects.select_related('companynumber').order_by(
            '{}companynumber__{}'.format('-' if  sortdirection=='decreasing' else '', sortby),
            'companynumber__companyname'
            )[:items]
    if ttype == 'basic':
        mach_titles = ['companyname', 'companynumber', 'siccode_sictext_1', 'regaddress_postcode', 'currentassets', 'fixedassets', 'totalassets', 'creditors', 'profitloss', 'turnoverrevenue', 'averagenumberemployeesduringperiod']
        table = []
        for item in query_set:
            table.append(get_data(mach_titles, item))

        return {'titles': [TITLE_LOOKUP[i] for i in mach_titles], 'table': table}


def get_data(mach_titles, item):    
    out = []
    for title in mach_titles:
        if title in company_titles:
            out.append(getattr(getattr(item, 'companynumber'), title))
        else:
            out.append(getattr(item, title) if getattr(item,title) else '')
    return out

company_titles = [
    'companyname', 
    'companynumber', 
    'regaddress_careof', 
    'regaddress_pobox', 
    'regaddress_addressline1', 
    'regaddress_addressline2', 
    'regaddress_posttown', 
    'regaddress_county', 
    'regaddress_country', 
    'regaddress_postcode', 
    'companycategory', 
    'companystatus', 
    'countryoforigin', 
    'dissolutiondate', 
    'incorporationdate', 
    'accounts_accountrefday', 
    'accounts_accountrefmonth', 
    'accounts_nextduedate', 
    'accounts_lastmadeupdate', 
    'accounts_accountcategory', 
    'returns_nextduedate', 
    'returns_lastmadeupdate', 
    'mortgages_nummortcharges', 
    'mortgages_nummortoutstanding', 
    'mortgages_nummortpartsatisfied', 
    'mortgages_nummortsatisfied', 
    'siccode_sictext_1', 
    'siccode_sictext_2', 
    'siccode_sictext_3', 
    'siccode_sictext_4', 
    'limitedpartnerships_numgenpartners', 
    'limitedpartnerships_numlimpartners', 
    'url', 
    'previousname_1_condate', 
    'previousname_1_companyname', 
    'previousname_2_condate', 
    'previousname_2_companyname', 
    'previousname_3_condate', 
    'previousname_3_companyname', 
    'previousname_4_condate', 
    'previousname_4_companyname', 
    'previousname_5_condate', 
    'previousname_5_companyname', 
    'previousname_6_condate', 
    'previousname_6_companyname', 
    'previousname_7_condate', 
    'previousname_7_companyname', 
    'previousname_8_condate', 
    'previousname_8_companyname', 
    'previousname_9_condate', 
    'previousname_9_companyname', 
    'previousname_10_condate', 
    'previousname_10_companyname', 
    'confstmtnextduedate', 
    'confstmtlastmadeupdate', 
    ]
