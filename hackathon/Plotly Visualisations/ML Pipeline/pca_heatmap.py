import numpy as np
from numpy import array
import pandas as pd
import plotly
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
# import plotly.graph_objs as graph_objs
import json
import pickle
plotly.tools.set_credentials_file(username='dhruvkuchhal', api_key='yUqN0qV3sFG4bMAfVjE1')
df = pickle.load(open('df_pca.sav', 'rb'))

# print (df)
# exit()
# data1 = pd.read_csv('cities_r2.csv')
#
# data1['latitude'] = data1['location'].apply(lambda x: float(x.split(',')[0]))
# data1['longitude'] = data1['location'].apply(lambda x: float(x.split(',')[1]))
#
# data1.drop(['state_code','dist_code','0-6_population_total','0-6_population_male','0-6_population_female',
#           'child_sex_ratio','latitude','longitude'], inplace=True, axis=1)
#
# data1 = data1.corr()
# print (data1.corr())

# for index, row in data1.iterrows():

data = [
    go.Heatmap(
        z=df.values.tolist(),
        x=df.keys(),
        y=df.index.tolist()
    )
]

layout = go.Layout(
    title = "Principal Components as linear combinations of various features",
    # titlefont = dict(
    #     size = '48'
    # ),
    font = dict(
        # size = '18',
        family = 'Raleway'
    ),
    # paper_bgcolor='#eeeeee',
    autosize = True,
    # font = dict(
    #     size = "11"
    # ),
    titlefont = dict(
        # color = '#8c9eac',
        size = '25'
    ),
    # legend = dict(
    #     orientation = 'h'
    # )
    # margin = dict(
    #     r = 200
    # )

    # width = '919',
    # height = '700'
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'pca_heatmap', show_link = False)))
# print tls.get_embed(py.plot(fig))
# with open('cities_max_jobs_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
