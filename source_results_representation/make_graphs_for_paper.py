'''
script to create an evaluation figure for a paper


Author: Anton Yeshchenko
'''


import csv
from pathlib import Path

from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
import re

#folder with validaiton resulis
path_to_log = Path("RESULTS_VAL_FINAL")
import glob, os
os.chdir(path_to_log)

resultFiles = list()
resultFileReaders = list()

logs = ["BPI2012", "BPI2017", "BPI2013", "Road_Traffic_Fine"]
type_index_based = "index-based"
type_last_state = "last-state"

enrichments_available_set = {"before","day","window"}
trace_style_dict= dict()
trace_style_dict["before"] = dict(name='before', legendgroup='trace1', line=dict(color='red'))
trace_style_dict["day"] = dict(name='day', legendgroup='trace2', line=dict(color='blue'))
trace_style_dict["window"] = dict(name='window', legendgroup='trace3', line=dict(color='green'))
trace_style_dict["none"] = dict(name='none', legendgroup='trace4', line=dict(color='orange'))


trace_param_dict= dict()

for log in logs:
    for file in glob.glob("*"+log+"*" + "ni" + "*"):
        #this is to find the encoding methosd
        found_string = re.findall(re.compile((log+'_.*?\_')), file)[0]
        found_string = found_string[len(log)+1:-1]

        log_csvfile = open(path_to_log / file, 'r')

        logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL, skipinitialspace=True)

        logheader = next(logreader, None)

        x = []
        y = []
        for logrow in logreader:
            if logrow[5] == "mae":
                x.append(int(logrow[4]))
                y.append(float(logrow[6]))

        if not (log + type_index_based) in trace_param_dict:
            trace_param_dict[log + type_index_based] = []
        if not found_string in enrichments_available_set:
            trace_param_dict[log+type_index_based].append([x,y, file, trace_style_dict["none"]])
        else:
            trace_param_dict[log+type_index_based].append([x, y, file, trace_style_dict[found_string]])

    for file in glob.glob("*"+log+"*" + "nl" + "*"):
        #this is to find the encoding methosd
        found_string = re.findall(re.compile((log+'_.*?\_')), file)[0]
        found_string = found_string[len(log)+1:-1]

        log_csvfile = open(path_to_log / file, 'r')

        logreader = csv.reader(log_csvfile, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL, skipinitialspace=True)

        logheader = next(logreader, None)

        x = []
        y = []
        for logrow in logreader:
            if logrow[5] == "mae":
                x.append(int(logrow[4]))
                y.append(float(logrow[6]))
        if not (log+type_last_state) in trace_param_dict:
            trace_param_dict[log+type_last_state] = []
        if not found_string in enrichments_available_set:
            trace_param_dict[log+type_last_state].append([x,y, file, trace_style_dict["none"]])
        else:
            trace_param_dict[log+type_last_state].append([x,y, file, trace_style_dict[found_string]])


fig = tools.make_subplots(rows=2, cols=4, subplot_titles=('BPI2012 index-based',
                                                          'BPI2013 index-based',
                                                          'BPI2017 index-based',
                                                          'Road traffic fine index-based',
                                                          'BPI2012 last-state',
                                                          'BPI2013 last-state',
                                                          'BPI2017 last-state',
                                                          'Road traffic fine last-state'))


styles = dict()
increment_x = 1

counter = 0
positions_of_plots = [(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4)]

keys_to_iterate_custom = ["BPI2012" + type_index_based,
                          "BPI2013" + type_index_based,
                          "BPI2017" + type_index_based,
                          "Road_Traffic_Fine" + type_index_based,
                          "BPI2012" + type_last_state,
                          "BPI2013" + type_last_state,
                          "BPI2017" + type_last_state,
                          "Road_Traffic_Fine" + type_last_state]

to_show_legend_correctly = {"before","day","window", "none"}
for key in keys_to_iterate_custom: # trace_param_dict.keys():
    pos_x, pos_y = positions_of_plots[counter]
    for one_enrichment in trace_param_dict[key]:

        trace_temp = go.Scatter(one_enrichment[3],
                                x=one_enrichment[0],
                                y=one_enrichment[1],
                                showlegend=(one_enrichment[3]["name"] in to_show_legend_correctly))
        if (one_enrichment[3]["name"] in to_show_legend_correctly):
            to_show_legend_correctly.remove(one_enrichment[3]["name"])
        fig.append_trace(trace_temp, pos_x, pos_y)
    counter += 1

#
# trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
# trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
# trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
# trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])
#
# fig.append_trace(trace1, 1, 1)
# fig.append_trace(trace2, 1, 2)
# fig.append_trace(trace3, 2, 1)
# fig.append_trace(trace4, 2, 2)

fig['layout'].update(height=1200, width=1200, title='Multiple Subplots' +
                                                  ' with Titles')

py.plot(fig, filename='make-subplots-multiple-with-titles')