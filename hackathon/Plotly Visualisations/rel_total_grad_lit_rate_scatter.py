import numpy as np
from numpy import array
import pandas as pd
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='sominwadhwa', api_key='MPdahdMDsEvh11ffGZdB')
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.basemap import Basemap
# import seaborn as sns

data = pd.read_csv('cities_r2.csv')
mean_graduates = data.total_graduates.mean()
max_graduates = data.total_graduates.max()
min_graduates = data.total_graduates.min()
graduates_data = data['total_graduates'].apply(lambda x: (x - mean_graduates ) / (max_graduates -min_graduates ))

mean_literates1 = data.effective_literacy_rate_total.mean()
max_literates1 = data.effective_literacy_rate_total.max()
min_literates1 = data.effective_literacy_rate_total.min()
literates_data1 = data['effective_literacy_rate_total'].apply(lambda x: (x - mean_literates1 ) / (max_literates1 -min_literates1 ))

print (graduates_data)
print (literates_data1)
# exit()
trace0 = go.Scatter(
    x = literates_data1,
    y = graduates_data,
    mode = 'markers'
)

data = [trace0]

layout = go.Layout(
    title = "Total Graduates vs<br>Literacy Rate in a State",
    titlefont = dict(
        size = '25'
    ),
    font = dict(
        # size = '18',
        family = "Raleway"
    ),
    xaxis = dict(
        title = "Literates",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Graduates",
        # titlefont = dict(
        #     size = '24'
        # )
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig,filename = 'rel_total_grad_lit_rate_scatter', show_link = False)))
# py.plot(fig, filename = 'rel_btw_gpa_salary_scatter.html', show_link = False)
# with open('rel_btw_gpa_salary_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
