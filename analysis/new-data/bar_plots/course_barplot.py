from utils import data_generator

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')

def plot(data):
    data = pd.DataFrame(data)
    data = data[data.X_TOTAL_STUDENTS !=0]
    data['target'] = (data.NO_OF_STUDENTS_PLACED / data.X_TOTAL_STUDENTS ) * 100
    data.target.fillna(0, inplace=True)
    data = data[['COURSE', 'target']]
    course_groupby = data.groupby(by='COURSE')['target'].mean()

    course_groupby.sort_values(ascending=False, inplace=True)
    course_groupby = course_groupby.head(20)

    trace = go.Bar(
        x = course_groupby.index,
        y = course_groupby,
        marker = dict(
        color = 'orange'
        )
    )
    data = [trace]
    layout = go.Layout(
        title = "Average Target values of 20 different courses in descending order",
        yaxis = dict(
            title = "Target"
        )
    )
    fig = go.Figure(data=data, layout= layout)
    print (tls.get_embed(py.plot(fig)))
