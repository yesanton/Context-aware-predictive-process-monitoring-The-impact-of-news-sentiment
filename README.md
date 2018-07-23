# Context-aware-predictive-process-monitoring-The-impact-of-news-sentiment
This repository contains scripts for using sentiment data from news, to annotate business event logs. This implementation is a part of the project-paper submitted to CoopIS 2018 conference. 

In order to run the code you must have sentiment files available (the example is in the folder SENTIMENT_SAMPLE_FILES)

1. Preprocess event log (remove unncessary columns) (2_delete_columns.py)
2. Decide if your log contains countries information (and check which ones you need) (also use 2_find_unique_countries.py)
3. Parse sentiment files (1_parse_file_sentiment_BPI2013_with_countries_to_make_it_compact.py, 1_parse_file_sentiment_to_make_it_compact.py)
4. Enrich event logs (3_annotate.py)
5. Run predictive algorithms (https://github.com/nirdizati/nirdizati-training-backend) (sample configurations are in folder)
6. Make different kinds of resutls and analysis (source_results.representation/*)

Enjoy the research! 


