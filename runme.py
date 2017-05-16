'''
Created on 16 May 2017

@author: pow-pow
'''

import csv
from pageaccess import PageImageDownloader

# Facebook app credentials
app_id = "CHANGEME"
app_secret = "CHANGEME"
TOKEN = app_id + "|" + app_secret

with open('batch.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        p = PageImageDownloader(row[0], row[1], row[2], int(row[3]), TOKEN)
        p.start()
