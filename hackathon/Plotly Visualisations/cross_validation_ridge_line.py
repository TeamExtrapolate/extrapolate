import numpy as np
from numpy import array
import pandas as pd
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
import pickle
plotly.tools.set_credentials_file(username='sharmaakshay', api_key='Q7PPhpMRXKFpL1SUnHm4')

cvScores_ridge = pickle.load(open('cvScores_ridge.sav', 'rb'))

x = []
y = []

for index in cvScores_ridge.index.values:
    x.append(index)
    y.append(cvScores_ridge[index])
# print (cvScores_ridge[cvScores_ridge.index.values[0]])
# Create a trace
trace = go.Scatter(
    x = x,
    y = y
)

data = [trace]

layout = go.Layout(
    title = "Cross Validation (Ridge)",
    titlefont = dict(
        size = '25'
    ),
    font = dict(
        # size = '18'
        family = "Raleway"
    ),
    xaxis = dict(
        title = "alpha (regularization parameter)",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Error",
        # titlefont = dict(
        #     size = '24'
        # )
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig,filename = 'cross_validation_ridge_line', show_link = False)))
