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

# pca = pickle.load(open('pca.sav', 'rb'))
# Y_pca = pickle.load(open('Y_pca.sav', 'rb'))
cumsum = pickle.load(open('cumsum.sav','rb'))

# print(cumsum)
# exit()

# x = []
# y = []
#
# for index in cvScores_ridge.index.values:
#     x.append(index)
#     y.append(cvScores_ridge[index])
# print (cvScores_ridge[cvScores_ridge.index.values[0]])
# Create a trace

# print (range(len(cumsum)))
# exit()
trace = go.Scatter(
    x = list(range(1, len(cumsum) + 1)),
    y = cumsum,
    x0 = 0,
    dx = 1
)

data = [trace]

layout = go.Layout(
    title = "Variance Retention as a function of<br>number of Principal Components",
    titlefont = dict(
        size = '20'
    ),
    # font = dict(
    #     size = '18'
    # ),
    xaxis = dict(
        title = "Number of Principal Components",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "(%) variance retained",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    font = dict(
        # size = "11",
        family = 'Raleway',
    ),
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig,filename = 'cummulative_variance_line', show_link = False)))
