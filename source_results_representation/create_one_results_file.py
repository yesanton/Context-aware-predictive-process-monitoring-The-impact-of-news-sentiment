'''
For each log, create a big table of detailed results in one csv file.

Author: Anton Yeshchenko
'''


import csv
from pathlib import Path


path_to_log = Path("/home/yesant/Documents/ProgrammingProjects/ParseRioNewsLogs/RESULTS_VAL_FINAL_per_log/BPI2017")

log = "BPI2017"

path_to_log = Path("/home/yesant/Documents/ProgrammingProjects/ParseRioNewsLogs/RESULTS_VAL_FINAL_per_log/BPI2012")

log = "BPI2012"


path_to_log = Path("/home/yesant/Documents/ProgrammingProjects/ParseRioNewsLogs/RESULTS_VAL_FINAL_per_log/BPI2013")

log = "BPI2013"


import glob, os
os.chdir(path_to_log)

resultFiles = list()
resultFileReaders = list()

for file in glob.glob("*"+log+"*"):
    print(file)
    resultFiles.append(file)

    log_csvfile = open(path_to_log  / file, 'r')
    logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL, skipinitialspace=True)

    resultFileReaders.append(logreader)


writer = csv.writer(open(path_to_log / (log + ".csv"), 'w'))



row1 = next(resultFileReaders[0], None)
row1[len(row1)-1] = resultFiles[0]

for i in range(len(resultFileReaders)-1):
    next(resultFileReaders[i+1], None)
    row1.append(resultFiles[i+1])


writer.writerow(row1)

for row1 in resultFileReaders[0]:
    for i in resultFileReaders[1:]:
        row = next(i, None)
        row1.append(row[-1])
    writer.writerow(row1)


