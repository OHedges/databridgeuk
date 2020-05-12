#!/usr/local/bin/python3

import zipfile
import os
from getfiles import Datascraper
import psycopg2
from config import config


# define wanted info for table headers
ID = 'UKCompaniesHouseRegisteredNumber'
with open('/usr/src/app/python/counts2') as f:
    content = f.readlines()

content = [x.rstrip(', \n') for x in content]

# find name of zipfile in /app/mediafiles/
directory = '/usr/src/app/mediafiles/'
#if len(os.listdir(directory)) != 1:
#    raise Exception('Wrong number of files in {}'.format(directory))
#else:
#    zipname = os.listdir(directory)[0]


# unzip zipfile to /app/mediafiles/
#with zipfile.ZipFile(directory + zipname, 'r') as zip_ref:
#    zip_ref.extractall(directory)


# move old zip to backup
#os.rename(directory + zipname, '/usr/src/app/zip_backup/{}'.format(zipname))

# connect to postgresql database and create cursor
conn = psycopg2.connect(**config())
cur = conn.cursor()

# scrape all files in /app/mediafiles/
#for item in os.listdir(directory)[:11]:
#    scrape = Datascraper(directory + item)
#    if scrape.is_dormant():
#        continue
#    output = scrape.get_id() + scrape.get_num(content)
#    
#    print(item)
#    print(output)

# insert scraped data into postgresql table
sql = 'INSERT INTO scraped_data'

# tmp
sql = """COPY basic_data FROM STDIN WITH (DELIMITER ',', FORMAT csv, HEADER, FORCE_NULL(accounts_accountrefday, accounts_accountrefmonth, mortgages_nummortcharges,mortgages_nummortoutstanding,mortgages_nummortpartsatisfied,mortgages_nummortsatisfied,limitedpartnerships_numgenpartners,limitedpartnerships_numlimpartners)) """
with open('/usr/src/app/BasicCompanyData-2020-05-01-part6_6.csv') as f:
    cur.copy_expert(sql, f)

#with open('/usr/src/app/test2.csv') as f:
#    cur.copy_from(f, 'basic_data', sep=",")

#sql = "COPY basic_data FROM '/usr/src/app/BasicCompanyData-2020-05-01-part6_6.csv' DELIMITER ','"
#cur.execute(sql)


# tmp



# commit changes to the database and close connection
conn.commit()
cur.close()
conn.close()

# delete all files in /app/mediafiles/
#directory = '/usr/src/app/mediafiles/'
#filelist = [f for f in os.listdir(directory)]
#for f in filelist:
#    os.remove(os.path.join(directory, f))
