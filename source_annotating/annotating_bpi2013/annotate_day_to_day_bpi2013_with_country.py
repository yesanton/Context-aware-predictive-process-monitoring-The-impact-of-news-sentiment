'''

annotate 2013 with day enrichment

Author: Anton Yeshchenko
'''


import csv
import json
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

def annotate_day_bpi2013(path_to_log,eventlog,sentiment_file ):
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
    writer.writerow(logheader + sentimentheader[2:])

    log_date_column= 3
    date_column_sentiment = 1
    COUNTRY_COLUMN = 0

    sentiment_dict = dict()
    for sentiment_row in sentimentreader:
        date_temp = datetime.strptime(sentiment_row[date_column_sentiment][0:], '%Y-%m-%d')
        country_temp = sentiment_row[COUNTRY_COLUMN]

        if not date_temp in sentiment_dict:
            sentiment_dict[date_temp] = dict()
            sentiment_dict[date_temp][country_temp] = sentiment_row[2:]
        else:
            sentiment_dict[date_temp][country_temp] = sentiment_row[2:]

    for log_row in logreader:
        log_date = datetime.strptime(log_row[log_date_column][0:10], '%Y/%m/%d')

        log_country = log_row[4]
        if log_date in sentiment_dict:
            if log_country in sentiment_dict[log_date]:
                print (log_country + "    " +  json.dumps(sentiment_dict[log_date]))
                writer.writerow(log_row + sentiment_dict[log_date][log_country])
            else:
                writer.writerow(log_row + [0, 0])
        else:
            # TODO if this case every happends, change the code
            writer.writerow(log_row + [0,0])

