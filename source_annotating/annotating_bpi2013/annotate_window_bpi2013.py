'''
bpi2013 with windows enrichment


Author: Anton Yeshchenko
'''


import csv
from pathlib import Path
from datetime import datetime
from datetime import timedelta

path_to_log = Path("/home/yesant/Documents/Data/ProcessMining/RioPaper_ExternalContextBPM/Fernando_2July")

folder_with_logs = "processed_logs_cut_for_available_data"
folder_with_sentiment_files = "processed"

folder_to_save_annotated = "3_window_annotated"

# here is even log to change!!!!!!!!

# eventlog = "BPI2017_1.csv"
# sentiment_file = "news-analysis.summary-2016.csv"
#
# eventlog = "BPI2013_not_filtered_colunms_removed.csv"
# sentiment_file = "news-analysis.summary-bpic2013-logs-2.csv"

#eventlog = "BPI2012.csv"
#sentiment_file = "news-analysis.summary-2012.csv"

def try_to_find_date_in_the_window_of_time(log_date, log_row, sentiment_dict, writer, window_size = 5):
    for i in range(1, window_size):
        if (log_date - timedelta(days=i)) in sentiment_dict:
            writer.writerow(log_row + sentiment_dict[log_date - timedelta(days=i)])
            return True
    return False


def annotate_window_bpi2013(path_to_log,eventlog,sentiment_file, window_size = 5):

    log_csvfile = open(path_to_log / folder_with_logs / eventlog, 'r')
    logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL, skipinitialspace=True)
    logheader = next(logreader, None)


    sentiment_csvfile = open(path_to_log / folder_with_sentiment_files / sentiment_file, 'r')
    sentimentreader = csv.reader(sentiment_csvfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL, skipinitialspace=True)
    sentimentheader = next(sentimentreader, None)


    writer = csv.writer(open(path_to_log / folder_to_save_annotated / eventlog, 'w'))
    writer.writerow(logheader + sentimentheader[1:])

    log_case_id_ind = 0

    log_date_column = 3
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


    #here we store case id dict in order to know if we already have case started
    case_ids_set = set()
    prev_date = None


    for log_row in logreader:
        log_date = datetime.strptime(log_row[log_date_column][0:10], '%Y/%m/%d')
        log_country = log_row[4]
        # here means that it is not the first event in the
        sum = [0,0]
        normalize_coefficient = 0
        prev_date = log_date - timedelta(days=window_size - 1)
        while prev_date <= log_date:
            if prev_date in sentiment_dict and log_country in sentiment_dict[prev_date]:
                normalize_coefficient += 1
                temp_sent_of_this_day = [float(i) for i in sentiment_dict[prev_date][log_country]]
                sum = [sum[i] + temp_sent_of_this_day[i] for i in range(len(sum))]
            prev_date += timedelta(days=1)
        if normalize_coefficient == 0:
            writer.writerow(log_row + sum)
        else:
            writer.writerow(log_row + [sum[i] / normalize_coefficient for i in range(len(sum))])