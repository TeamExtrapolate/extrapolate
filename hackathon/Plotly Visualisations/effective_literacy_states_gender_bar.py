import numpy as np
from numpy import array
import pandas as pd
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='aviralgupta', api_key='1gKSa84X3l2px8iQ5BRJ')
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.basemap import Basemap
# import seaborn as sns

data = pd.read_csv('cities_r2.csv')
states = data[['literates_female','literates_male', 'state_name']].groupby('state_name',as_index=False).sum()

# print (states)
# print (states['state_name'])

trace0 = go.Bar(
    x = states['state_name'],
    y = states['literates_male'],
    name = "Male"
)

trace1 = go.Bar(
    x = states['state_name'],
    y = states['literates_female'],
    name = "Female"
)

data = [trace0, trace1]

layout = go.Layout(
    title = "Literacy by States",
    titlefont = dict(
        size = '25'
    ),
    xaxis = dict(
        title = "States",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Literacy Rate Total",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    barmode='stack'
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'literacy_states_gender_bar', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'salary_distribution_bar.html', show_link=False)
# with open('salary_distribution_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
