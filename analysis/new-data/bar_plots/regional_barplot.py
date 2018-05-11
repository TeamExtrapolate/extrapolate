from utils import data_generator

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')


data = data_generator(['INSTI_REGION'])
region_group = data.groupby(by='INSTI_REGION')['target'].mean()
trace = go.Bar(
    x = region_group.index,
    y = region_group
)
data = [trace]
layout = go.Layout(
    title = "Average Target values in different regions",
    yaxis = dict(
        title = "Target"
    ),
    xaxis = dict(
        title = "Region"
    )
)
fig = go.Figure(data=data, layout= layout)
print (tls.get_embed(py.plot(fig)))
