import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

import django
django.setup()

from django.db.models import Max
from upload.models import Accounts, SicCode, Company
from .lookup import title
from datetime import datetime

# creates a 1:1 dict for converting between mach and human titles
class TwoWay:
    def __init__(self):
        self.d = {}

    def add(self, k ,v):
        self.d[k] = v
        self.d[v] = k

    def remove(self, k):
        self.d.pop(self.d.pop(k))

    def get(self, k):
        return self.d[k]

def make_tables(sortby='companyname', direction='ascending', category='1'):
    if category == '1':
        sics = SicCode.objects.all()
        accos = Accounts.objects.all()
    else:
        sics = SicCode.objects.filter(category__title=cat.get(category))
        comps = Company.objects.filter(siccodes__in=sics)
        accos = Accounts.objects.filter(companynumber__in=comps)
    accos = accos.order_by(
            get_order(sortby, direction),
            'companynumber__companyname'
            )[:1000]
    table = {'titles':[get_field(i) for i in mach_titles], 'body': []}
    for item in accos:
        table['body'].append(get_data(mach_titles, item))
    return table


def get_order(item, direction):
    if item in company_titles:
        return '{}companynumber__{}'.format('' if direction=='ascending' else '-', item)
    else:
        return '{}{}'.format('' if direction=='ascending' else '-', item)


def get_data(mach_titles, item):    
    out = []
    for title in mach_titles:
        if title in company_titles:
            out.append(getattr(getattr(item, 'companynumber'), title) or '')
        else:
            out.append(getattr(item, title) or '')
    return out


# parses fields collected from django models
def parse_fields(fields):
    return [str(f).split('.')[-1] for f in fields[1:]]


# converts machine readable field heading to human readable
def get_field(field):
    return title.get(field, field)


# checks whether the given row contains no values
def is_empty(row):
    return row[1:] == len(row[1:]) * ['']


# parse text to be in acceptable url format
def make_url(txt):
    return txt.replace(' ', '_').replace('/', '_').lower()


mach_titles = ('companyname', 'companynumber', 'regaddress_postcode', 'currentassets', 'fixedassets', 'totalassets', 'creditors', 'profitloss', 'turnoverrevenue', 'averagenumberemployeesduringperiod')


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
cat = TwoWay()
for i,k in [('leasing', 'Leasing'), ('dormant', 'Dormant'), ('household', 'Household'), ('organisations', 'Organisations'), ('office_administration', 'Office/Administration'), ('real_estate', 'Real Estate'), ('insurance', 'Insurance'), ('technology', 'Technology'), ('legal', 'Legal'), ('finance', 'Finance'), ('retail', 'Retail'), ('electricity_electronics', 'Electricity/Electronics'), ('packaging_storage', 'Packaging/Storage'), ('waste', 'Waste'), ('plastics', 'Plastics'), ('chemicals', 'Chemicals'), ('tools_furniture', 'Tools/Furniture'), ('media_communications', 'Media/Communications'), ('medicine_care_security', 'Medicine/Care/Security'), ('entertainment_leisure', 'Entertainment/Leisure'), ('education', 'Education'), ('transport', 'Transport'), ('construction_maintenance', 'Construction/Maintenance'), ('wholesale', 'Wholesale'), ('processing', 'Processing'), ('manufacturing', 'Manufacturing'), ('paper', 'Paper'), ('textiles_fashion', 'Textiles/Fashion'), ('oil_gas_mining_extraction', 'Oil/Gas/Mining/Extraction'), ('consumables', 'Consumables'), ('plants_animals_fish', 'Plants/Animals/Fish'), ('metals_metal_products', 'Metals/Metal Products'), ('non-trading', 'Non-Trading')]:
    cat.add(i,k)
