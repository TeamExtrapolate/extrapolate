from utils import data_generator

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

from itertools import groupby
from operator import itemgetter

plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')

# data = data_generator(['INSTI_STATE'])
# state_group = data.groupby(by='INSTI_STATE')['target'].mean()

def plot(data):

    grouper = itemgetter("COURSE")
    result = []
    for key, grp in groupby(sorted(data, key=grouper), grouper):
        temp_dict = dict(zip(["COURSE"], [key]))
        temp_list = [item["target"] for item in grp]
        temp_dict['target'] = sum(temp_list) / len(temp_list)
        result.append(temp_dict)

    data = sorted(result, key = itemgetter("target"), reverse=True)
    data = data[0:20]

    x = []
    y = []
    for item in data:
        x = x + [item['COURSE']]
        y = y + [item['target']]


    trace = go.Bar(
        x = x,
        y = y
    )
    data = [trace]
    layout = go.Layout(
        title = "Average Target values in different states",
        yaxis = dict(
            title = "Target"
        ),
        xaxis = dict(
            title = "States"
        )
    )
    fig = go.Figure(data=data, layout= layout)
    return fig
    # print (tls.get_embed(py.plot(fig)))
