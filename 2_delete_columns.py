'''
SCRIPT TO CLEAN THE LOG out off unnecessary cluttering columns


Author: Anton Yeshchenko
'''


import csv
from pathlib import Path

path_to_log = Path(
    "path/to/cleaned/event/log")

#This is for BPI2017
eventlog = "BPI2013.csv"
eventlog_out = "BPI2013_prepared.csv"
keep_columns_indeces = [0,1,2,3,8]



csvfile = open(path_to_log / eventlog, 'r')

logreader = csv.reader(csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL, skipinitialspace=True)


writer = csv.writer(open(path_to_log / eventlog_out, 'w'))



for row in logreader:
    writer.writerow([row[i] for i in keep_columns_indeces])




