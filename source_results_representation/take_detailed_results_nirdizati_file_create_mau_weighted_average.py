'''
calculate mae and srd


Author: Anton Yeshchenko
'''

import csv
from math import sqrt
from pathlib import Path

path_to_log = Path("/home/yesant/Documents/ProgrammingProjects/ParseRioNewsLogs/RESULTS_DETAILED_FINAL")

import glob, os
os.chdir(path_to_log)

resultFiles = list()
resultFileReaders = list()

writer = csv.writer(open(path_to_log / "all_detailed.csv", 'w'))

for file in glob.glob("*r.csv"):


    log_csvfile = open(path_to_log / file, 'r')
    logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, skipinitialspace=True)

    next(logreader, None)
    mae = 0
    std = 0
    counter = 0
    vector_calculate_std = []
    for i in logreader:
        predicted = float(i[7])
        actual = float(i[0])
        diff = predicted - actual
        vector_calculate_std.append(abs(diff))
        mae += abs(diff)
        #i[6] # number of events
        counter += 1

    mae /= counter
    for item in vector_calculate_std:
        std += (mae -item) * (mae -item)
    std /= (counter - 1)
    std = sqrt(std)

    writer.writerow([file,"%.3f" % mae, "%.3f" % std])
