import numpy as np
from numpy import array
import pandas as pd
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')

data = pd.read_csv('cities_r2.csv')
grouped_data = data.groupby('state_name')
grouped_data_mean = grouped_data.mean().reset_index()

trace0 = go.Bar(
    x = grouped_data_mean['total_graduates'],
    # marker = dict(
    #     color = "#feda62"
    # ),
    y = grouped_data_mean['state_name'],
    orientation = 'h'

)

data = [trace0]

layout = go.Layout(
    title = "<br>Graduates per State",
    titlefont = dict(
        size = '25',
        color = '#8c9eac'
        # color = "#000000"
    ),
    font = dict(
        # size = '10',
        family = 'Roboto',
        color = "#000000"
    ),
    # paper_bgcolor='#eeeeee',
    xaxis = dict(
        title = "Total Graduates",
        # titlefont = dict(
        #     size = '18',
        #     color = '#8c9eac'
        # )
    ),
    yaxis = dict(
        title = "Name of State",
        # titlefont = dict(
        #     size = '18',
        #     color = '#8c9eac'
        # )
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'graduates_bar',  show_link = False, auto_open = False)))
# print tls.get_embed(py.plot(fig, filename = 'top_ten_highest_paying_jobs_bar', link = False, show_link = False, auto_open = False))
# py.plot(fig, filename = 'top_ten_highest_paying_jobs_bar.html', show_link=False)
# with open('top_ten_highest_paying_jobs_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
