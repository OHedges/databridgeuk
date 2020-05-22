import os
from bs4 import BeautifulSoup

def name_from_ix_element(e):
    return e.get('name').split(':', 1)[-1]

class DataScraper:
    def __init__(self, path):
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
        num_dict = {k: [] for k in wanted} # use dict.setdefualt() later instead
        for k, v in num:
            parsed_v = v.split('.')[0].replace(',', '').replace(' ','').replace('\\n', '').replace('--','-')
            try:
                num_dict[k].append('' if v == '-' else int(parsed_v))
            except KeyError:
                continue
        line = []
        for k in wanted:
            vs = num_dict[k][-2:] # take at most last two from scraped values
            line.append('' if len(vs) == 0 else vs[0])
        return line

    def get_id(self):
        ix_info = self.soup.find_all('ix:nonnumeric')
        ixs = [(name_from_ix_element(i), i.text) for i in ix_info]
        for name, text in ixs:
            if name == 'UKCompaniesHouseRegisteredNumber':
                return [text]
        return ['Error: no ID']
