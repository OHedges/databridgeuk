import sys
sys.path.append('/usr/src/app/')

from upload.getaccounts import get_accounts

urls = ['http://download.companieshouse.gov.uk/Accounts_Bulk_Data-2020-05-28.zip']

for url in urls:
    get_accounts(url)
