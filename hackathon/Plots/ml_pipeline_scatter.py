import numpy as np
from numpy import array
import pandas as pd
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
from plotly import tools
import plotly.graph_objs as go
import plotly
import pickle
plotly.tools.set_credentials_file(username='sominwadhwa', api_key='MPdahdMDsEvh11ffGZdB')
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.basemap import Basemap
# import seaborn as sns

train = pickle.load(open('train.sav', 'rb'))
train.Salary = np.log1p(train.Salary)

print (train)

# print (Y)

# exit()
#
# data = pd.read_csv('cities_r2.csv')
# mean_graduates = data.total_graduates.mean()
# max_graduates = data.total_graduates.max()
# min_graduates = data.total_graduates.min()
# graduates_data = data['total_graduates'].apply(lambda x: (x - mean_graduates ) / (max_graduates -min_graduates ))
#
# mean_literates1 = data.effective_literacy_rate_total.mean()
# max_literates1 = data.effective_literacy_rate_total.max()
# min_literates1 = data.effective_literacy_rate_total.min()
# literates_data1 = data['effective_literacy_rate_total'].apply(lambda x: (x - mean_literates1 ) / (max_literates1 -min_literates1 ))

# print (graduates_data)
# print (literates_data1)

trace1 = go.Scatter(
    x = train['12percentage'],
    y = train['Salary'],
    mode = 'markers'
)

trace2 = go.Scatter(
    x = train['mcolgGPA'],
    y = train['Salary'],
    mode = 'markers'
)

fig = tools.make_subplots(rows = 1, cols = 2, horizontal_spacing = 0.20, )
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(
    # font = dict(
    #     size = '18'
    # )
)

fig['layout'].update(
    # title = "Normalization of Salaries",
    showlegend = False,
    # margin = dict(
    #     pad = 100
    # )
    titlefont = dict(size='25')
)

fig['layout']['xaxis2'].update(
    title = "College GPA",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['yaxis2'].update(
    title = "Salary",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['xaxis1'].update(
    title = "12th class Percentage",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['yaxis1'].update(
    title = "Salary",
    # titlefont = dict(
    #     size = '24'
    # )
)


# data = [trace0]
#
# layout = go.Layout(
#     title = "Relation between Total Graduates and Literacy Rate in a State",
#     titlefont = dict(
#         size = '25'
#     ),
#     # font = dict(
#     #     size = '18'
#     # ),
#     xaxis = dict(
#         title = "12th Percentage",
#         # titlefont = dict(
#         #     size = '24'
#         # )
#     ),
#     yaxis = dict(
#         title = "Salary",
#         # titlefont = dict(
#         #     size = '24'
#         # )
#     )
# )
#
# fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig,filename = 'ml_pipeline_scatter', show_link = False)))
# py.plot(fig, filename = 'rel_btw_gpa_salary_scatter.html', show_link = False)
# with open('rel_btw_gpa_salary_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
