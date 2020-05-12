#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
import zipfile

class Datascraper:
    def __init__(self, path):
        self.soup = BeautifulSoup(open(path), 'lxml')
   
    def is_dormant(self):
        names = ['EntityDormantTruefalse','EntityDormant']
        ix = self.soup.find_all('ix:nonnumeric')
        for i in ix:
            if i.get('name').split(':', 1)[-1] in names and i.text == 'true':
                return True
        return False

    def get_num(self, wanted):
        ix_num = self.soup.find_all('ix:nonfraction')
        num = [[i.get('name').split(':',1)[-1], i.text, i.get('sign')] for i in ix_num]
        num_dict = {k: [] for k in wanted}
        for k, v, s in num:
            if k in wanted:
                num_dict[k].append(v) if s == None else num_dict[k].append('-' + v)
        line = []
        for a, b in num_dict.items():
            try:
                line.append(int('{}'.format(b[-2]).replace(',','')))
            except:
                line.append('')
        return line

    def get_id(self):
        ix_info = self.soup.find_all('ix:nonnumeric')
        ixs = [[i.get('name').split(':',1)[-1], i.text] for i in ix_info]
        for name, text in ixs:
            if name == 'UKCompaniesHouseRegisteredNumber':
                return [text]
        return ['Error: no ID']

