'''
annotating main script


Author: Anton Yeshchenko
'''


import csv
from builtins import set
from pathlib import Path
from datetime import datetime

from source_annotating.annotate_before import annotate_before
from source_annotating.annotate_day_to_day import annotate_day
from source_annotating.annotate_random import annotate_random
from source_annotating.annotate_window import annotate_window
from source_annotating.annotating_bpi2013.annotate_before_bpi2013 import annotate_before_bpi2013
from source_annotating.annotating_bpi2013.annotate_day_to_day_bpi2013_with_country import annotate_day_bpi2013
from source_annotating.annotating_bpi2013.annotate_window_bpi2013 import annotate_window_bpi2013

path_to_log = Path("//path/to/sentiment/files/and/eventlogs")

folder_with_logs = "processed_logs_cut_for_available_data"
folder_with_sentiment_files = "processed"

folder_to_save_annotated = "1_day_to_day_annotated"

# here is even log to change!!!!!!!!
eventlog = "BPI2017.csv"
sentiment_file = "news-analysis.summary-bpic2012-2017-logs-2.csv"


eventlog = "BPI2012.csv"
sentiment_file = "news-analysis.summary-bpic2012-logs-first-half-of-timerange.csv"


eventlog = "BPI2013.csv"
sentiment_file = "news-analysis.summary-bpic2013-logs-2.csv"

path_to_log = Path("/path/to/sentiment/files/and/eventlogs")
eventlog = "Road_Traffic_Fine.csv"
sentiment_file = "italian-logs-news-summary.csv"

#
# eventlog = "BPI2012.csv"
# sentiment_file = "news-analysis.summary-2012.csv"
#
# eventlog = "BPI2013_not_filtered_colunms_removed.csv"
# sentiment_file = "news-analysis.summary-bpic2013-logs-2.csv"
#
#
#annotate_day(path_to_log, eventlog, sentiment_file)
#annotate_before(path_to_log, eventlog, sentiment_file)
annotate_window(path_to_log, eventlog, sentiment_file)
#annotate_random(path_to_log, eventlog)



#TODO when source_annotating intoduces leftover column in the header of files
#annotate_day_bpi2013(path_to_log, eventlog, sentiment_file)
# annotate_before_bpi2013(path_to_log, eventlog, sentiment_file)
# annotate_window_bpi2013(path_to_log, eventlog, sentiment_file)
# annotate_random(path_to_log, eventlog)
