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

# DATA FORMAT = [{'STATE': state_name, 'X_TOTAL_STUDENTS': int, 'NO_OF_STUDENTS_PLACED':int}]
def plot(data):

    data = pd.DataFrame(data)
    data = data[data.X_TOTAL_STUDENTS !=0]
    data['target'] = (data.NO_OF_STUDENTS_PLACED / data.X_TOTAL_STUDENTS ) * 100
    data.target.fillna(0, inplace=True)
    data = data[['INSTI_STATE', 'target']]
    state_group = data.groupby(by='INSTI_STATE')['target'].mean()

    trace = go.Bar(
        x = state_group.index,
        y = state_group
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
