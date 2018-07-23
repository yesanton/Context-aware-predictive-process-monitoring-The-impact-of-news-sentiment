
'''
finds unique countries in the sentiment file


Author: Anton Yeshchenko
'''


import csv
from pathlib import Path

path_to_log = Path("/path/to/sentiment/files")

eventlog_arg = "italian-logs-news-summary.csv"

csvfile = open(path_to_log / eventlog_arg, 'r')

logreader = csv.reader(csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL, skipinitialspace=True)


id_country = 1

countries = set()

for i in logreader:
    countries.add(i[id_country])


print (countries)