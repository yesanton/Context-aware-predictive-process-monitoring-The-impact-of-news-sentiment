'''

experimental annotation with ranrom values

Author: Anton Yeshchenko
'''

import csv
from pathlib import Path
from datetime import datetime
import random
folder_with_logs = "processed_logs_cut_for_available_data"
folder_with_sentiment_files = "processed"

folder_to_save_annotated = "5_random_annotated"

# here is even log to change!!!!!!!!
# eventlog = "BPI2017_1.csv"
# sentiment_file = "news-analysis.summary-2016.csv"

#
# eventlog = "BPI2012.csv"
# sentiment_file = "news-analysis.summary-2012.csv"
#
# eventlog = "BPI2013_not_filtered_colunms_removed.csv"
# sentiment_file = "news-analysis.summary-bpic2013-logs-2.csv"

def annotate_random(path_to_log,eventlog):
    log_csvfile = open(path_to_log / folder_with_logs / eventlog, 'r')

    logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL, skipinitialspace=True)


    logheader = next(logreader, None)

    writer = csv.writer(open(path_to_log / folder_to_save_annotated / eventlog, 'w'))
    #write header
    writer.writerow(logheader + ["avg_body_wink_normalized_score","avg_body_sentiment_score"])

    for log_row in logreader:
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)

        writer.writerow(log_row + [r1,r2])

