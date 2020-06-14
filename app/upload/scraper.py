import os
from bs4 import BeautifulSoup
import datetime

def name_from_ix_element(e):
    return e.get('name').split(':', 1)[-1]

class DataScraper:
    def __init__(self, path):
        self.path = path
        self.soup = BeautifulSoup(open(path), 'lxml')
   
    def is_dormant(self):
        names = ('EntityDormantTruefalse','EntityDormant')
        for i in self.soup.find_all('ix:nonnumeric'):
            if i.text == 'true' and name_from_ix_element(i) in names:
                return True
        return False

    def get_num(self, wanted):
        ix_num = self.soup.find_all('ix:nonfraction')
        num = [(name_from_ix_element(i), i.get('sign', '') + i.text) for i in ix_num]
        num_dict = {k: [] for k in wanted}
        for k, v in num:
            parsed_v = v.split('.')[0].replace(',', '').replace(' ','').replace('--','-').replace('\n','')
            try:
                num_dict[k].append('' if parsed_v == '-' else int(parsed_v))
            except KeyError:
                continue
        line = []
        for k in wanted:
            vs = num_dict[k][-2:] # take at most last two from scraped values
            line.append('' if len(vs) == 0 else vs[0])
        return line

    def get_id(self):
        name = self.path.split('/')[-1]
        name = name.split('_')[2]
        return [name]

    def get_date(self):
        date = self.path.split('_')[-1]
        return datetime.date(int(date[:4]),int(date[4:6]),int(date[6:8]))
