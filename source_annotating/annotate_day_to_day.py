'''

annotate with day enrichment, (no locaiton info in the log)

Author: Anton Yeshchenko
'''


import csv
from pathlib import Path
from datetime import datetime

folder_with_logs = "processed_logs_cut_for_available_data"
folder_with_sentiment_files = "processed"

folder_to_save_annotated = "1_day_annotated"

# here is even log to change!!!!!!!!
# eventlog = "BPI2017_1.csv"
# sentiment_file = "news-analysis.summary-2016.csv"

#
# eventlog = "BPI2012.csv"
# sentiment_file = "news-analysis.summary-2012.csv"
#
# eventlog = "BPI2013_not_filtered_colunms_removed.csv"
# sentiment_file = "news-analysis.summary-bpic2013-logs-2.csv"

def annotate_day(path_to_log,eventlog,sentiment_file ):
    log_csvfile = open(path_to_log / folder_with_logs / eventlog, 'r')

    logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL, skipinitialspace=True)


    logheader = next(logreader, None)


    sentiment_csvfile = open(path_to_log / folder_with_sentiment_files / sentiment_file, 'r')

    sentimentreader = csv.reader(sentiment_csvfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL, skipinitialspace=True)

    sentimentheader = next(sentimentreader, None)



    writer = csv.writer(open(path_to_log / folder_to_save_annotated / eventlog, 'w'))
    #write header
    writer.writerow(logheader + sentimentheader[1:])

    log_date_column= 3
    date_column_sentiment = 0

    sentiment_dict = dict()
    for sentiment_row in sentimentreader:
        sentiment_dict[datetime.strptime(sentiment_row[date_column_sentiment][0:], '%Y-%m-%d')] = sentiment_row[1:]

    for log_row in logreader:
        log_date = datetime.strptime(log_row[log_date_column][0:10], '%Y/%m/%d')

        if log_date in sentiment_dict:
            writer.writerow(log_row + sentiment_dict[log_date])
        else:

            writer.writerow(log_row + [0,0])

