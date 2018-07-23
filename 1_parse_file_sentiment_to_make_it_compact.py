'''
this file parses the file of sentiment  for specific log
it find the matching countries and summarizes the sentiment for each one day

in case of missing values the previous day sentiment is taken

THIS SCRIPT IS USED IF THERE IS NO EXPLICIT LOCATION ASSOCIATED FOR EACH EVENT IN THE LOG

Author: Anton Yeshchenko

'''
import csv
import math
from pathlib import Path

from operator import itemgetter


eventlog = "news-analysis.summary-italian-logs.csv"
eventlog = "news-analysis.summary-2000.csv"
eventlogs = ["news-analysis.summary-2010.csv",
             "news-analysis.summary-2011.csv",
             "news-analysis.summary-2012.csv",
 "news-analysis.summary-2000.csv",   "news-analysis.summary-2013.csv",
 "news-analysis.summary-2001.csv",   "news-analysis.summary-2014.csv",
 "news-analysis.summary-2002.csv",  "news-analysis.summary-2015.csv",
 "news-analysis.summary-2003.csv",   "news-analysis.summary-2016.csv",
 "news-analysis.summary-2004.csv",   "news-analysis.summary-2017.csv",
 "news-analysis.summary-2005.csv",   "news-analysis.summary-bpic2012-logs.csv",
 "news-analysis.summary-2006.csv",   "news-analysis.summary-bpic2013-logs.csv",
 "news-analysis.summary-2007.csv",
 "news-analysis.summary-2008.csv",
 "news-analysis.summary-2009.csv",
#"news-analysis.summary-italian-logs.csv"
             ]

eventlogs = ["news-analysis.summary-2010.csv",
             "news-analysis.summary-2011.csv",
             "news-analysis.summary-2012.csv",
         "news-analysis.summary-2013.csv",
 "news-analysis.summary-2000.csv",
 "news-analysis.summary-2004.csv",
 "news-analysis.summary-2005.csv",
 "news-analysis.summary-2006.csv",
 "news-analysis.summary-2007.csv",
 "news-analysis.summary-2008.csv",
 "news-analysis.summary-2009.csv",
"news-analysis.summary-italian-logs.csv"
             ]

#news-analysis.summary-bpic2013-logs-2.csv



def parse_file(path_to_log, sentiment_file_arg, id_country,
               pub_date,
               avg_body_sentiment,
               avg_body_wink_normalized, countries_to_pick_from):

    csvfile = open(path_to_log / sentiment_file_arg, 'r')

    logreader = csv.reader(csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL, skipinitialspace=True)

    header = next(logreader, None)  # skip the headers


    writer = csv.writer(open(path_to_log / "processed" / sentiment_file_arg, 'w'))

    n_avg_body_sentiment = 2
    n_avg_body_wink_normalized = 3

    what_i_need_to_get_indeces = [id_country, pub_date, avg_body_sentiment, avg_body_wink_normalized]

    i = 0 #index_to_begin_normalization
    name_country_to_check = ""
    date_to_check = ""


    temp_list = list()

    first_mark = False

    # write to the file headers
    writer.writerow([header[ind] for ind in what_i_need_to_get_indeces[1:]])

    for row in logreader:

        #here we check for the country to be in our list
        if not row[id_country] in countries_to_pick_from:
            continue

        if (date_to_check != row[pub_date]):
            print (date_to_check)

# this line if we want to check and group also by country
#if first_mark and (name_country_to_check != row[id_country] or date_to_check != row[pub_date]):
        if first_mark and date_to_check != row[pub_date]:

            temp_avg_body_sentiment = 0
            temp_avg_body_wink_normalized = 0

            for i in temp_list:

                #print (i[n_avg_body_sentiment])
                if not i[n_avg_body_sentiment] == 'NaN' and not i[n_avg_body_sentiment] == '':
                    print (i)
                    temp_avg_body_sentiment += float(i[n_avg_body_sentiment])
                if not i[n_avg_body_wink_normalized] == 'NaN':
                    temp_avg_body_wink_normalized += float(i[n_avg_body_wink_normalized])

            if math.fabs(temp_avg_body_wink_normalized)< 0.0001:
                print ('THERE IS 0 FOR SOME DAY')

            temp_avg_body_sentiment /= len(temp_list)
            temp_avg_body_wink_normalized /= len(temp_list)


            #write to file here
# this line if also by country
#writer.writerow([name_country_to_check, date_to_check, temp_avg_body_sentiment, temp_avg_body_wink_normalized])
            writer.writerow(
                [date_to_check, temp_avg_body_sentiment, temp_avg_body_wink_normalized])

            name_country_to_check = row[id_country]
            date_to_check = row[pub_date]
            temp_list.clear()

        if not first_mark:
            name_country_to_check = row[id_country]
            date_to_check = row[pub_date]

        temp_list.append([row[ind] for ind in what_i_need_to_get_indeces])

        first_mark = True


# for eventl in eventlogs:
#     print("FILE NAME:  " + eventl)
#     parse_file(eventl)
#


# ####### BPI 2017
# path_to_log = Path("/home/yesant/Documents/Data/ProcessMining/"
#                    "RioPaper_ExternalContextBPM/Fernando_9July/")
# sentiment_file = "news-analysis.summary-bpic2012-2017-logs-2.csv"
# id_country = 1
# pub_date = 2
# avg_body_sentiment = 9
# avg_body_wink_normalized = 10
# countries_to_pick_from = { 'France, Metropolitan', 'Hungary', 'Yugoslavia', 'Serbia and Montenegro', 'Albania', 'Denmark',
#                             'Greenland',  'Vatican City State', 'Netherlands Antilles', 'Kosovo', 'Italy', 'Luxembourg', 'Bulgaria', 'Malta',  'Canary Islands',
#                            'Sweden', 'Ireland',  'Czech Republic',  'Slovakia',  'Colombia', 'European Union',  'Germany', 'Cyprus',
#                            'Poland',  'Austria','Netherlands', 'France', 'Finland', 'Belgium',  'Switzerland',  'Lithuania',
#                            'United Kingdom','Moldova', 'Greece',  'Norway', 'New Zealand', 'Romania','Iceland',
#                            'German Democratic Republic', 'Latvia', 'Turkey', 'Czechoslovakia', 'Portugal',
#                            'Liechtenstein' 'Serbia', 'Estonia', 'Slovenia', 'Croatia'}
#
#
#
# ####### BPI 2012
# path_to_log = Path("/home/yesant/Documents/Data/ProcessMining/"
#                    "RioPaper_ExternalContextBPM/Fernando_17July/")
# sentiment_file = "news-analysis.summary-bpic2012-logs-first-half-of-timerange.csv"
# id_country = 1
# pub_date = 2
# avg_body_sentiment = 9
# avg_body_wink_normalized = 10
# countries_to_pick_from = { 'France, Metropolitan', 'Hungary', 'Yugoslavia', 'Serbia and Montenegro', 'Albania', 'Denmark',
#                             'Greenland',  'Vatican City State', 'Netherlands Antilles', 'Kosovo', 'Italy', 'Luxembourg', 'Bulgaria', 'Malta',  'Canary Islands',
#                            'Sweden', 'Ireland',  'Czech Republic',  'Slovakia',  'Colombia', 'European Union',  'Germany', 'Cyprus',
#                            'Poland',  'Austria','Netherlands', 'France', 'Finland', 'Belgium',  'Switzerland',  'Lithuania',
#                            'United Kingdom','Moldova', 'Greece',  'Norway', 'New Zealand', 'Romania','Iceland',
#                            'German Democratic Republic', 'Latvia', 'Turkey', 'Czechoslovakia', 'Portugal',
#                            'Liechtenstein' 'Serbia', 'Estonia', 'Slovenia', 'Croatia'}




########
## Road traffic
path_to_log = Path("/home/yesant/Documents/Data/ProcessMining/"
                   "RioPaper_ExternalContextBPM/Fernando_22July/")
sentiment_file = "italian-logs-news-summary.csv"
id_country = 1
pub_date = 2
avg_body_sentiment = 9 #avg_body_sentiment_score
avg_body_wink_normalized = 10 #avg_body_wink_normalized_score
countries_to_pick_from = { 'France, Metropolitan', 'Hungary', 'Yugoslavia', 'Serbia and Montenegro', 'Albania', 'Denmark',
                            'Greenland',  'Vatican City State', 'Netherlands Antilles', 'Kosovo', 'Italy', 'Luxembourg', 'Bulgaria', 'Malta',  'Canary Islands',
                           'Sweden', 'Ireland',  'Czech Republic',  'Slovakia',  'Colombia', 'European Union',  'Germany', 'Cyprus',
                           'Poland',  'Austria','Netherlands', 'France', 'Finland', 'Belgium',  'Switzerland',  'Lithuania',
                           'United Kingdom','Moldova', 'Greece',  'Norway', 'New Zealand', 'Romania','Iceland',
                           'German Democratic Republic', 'Latvia', 'Turkey', 'Czechoslovakia', 'Portugal',
                           'Liechtenstein' 'Serbia', 'Estonia', 'Slovenia', 'Croatia'}



parse_file(path_to_log,sentiment_file, id_country ,
    pub_date ,
    avg_body_sentiment,
    avg_body_wink_normalized,
           countries_to_pick_from)





