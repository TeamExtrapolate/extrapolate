import numpy as np
from numpy import array
import pandas as pd
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='prashasti', api_key='r55iCiSMro8stYszHC0g')
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.basemap import Basemap
# import seaborn as sns

data = pd.read_csv('cities_r2.csv')
states = data[['effective_literacy_rate_total','state_name']].groupby('state_name',as_index=False).sum()

# print (states['state_name'])

trace0 = go.Bar(
    x = states['state_name'],
    y = states['effective_literacy_rate_total'],
    marker = dict(
        color = "#feda62"
    )
)

data = [trace0]

layout = go.Layout(
    title = "Effective Literacy by States",
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
        title = "Mean Effective Literacy",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    margin = dict(
        b = 120
    ),
    font = dict(
        family = "Raleway"
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'effective_literacy_states_bar', show_link = False)))
# py.plot(fig, filename = 'salary_distribution_bar.html', show_link=False)
# with open('salary_distribution_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
