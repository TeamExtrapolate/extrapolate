from utils import data_generator

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')

#DataFrame= {"PROGRAMME": value, "X_TOTAL_STUDENTS": int, "NO_OF_STUDENTS_PLACED":int}
def plot(data):
    data = pd.DataFrame(data)
    data = data[data.X_TOTAL_STUDENTS !=0]
    data['target'] = (data.NO_OF_STUDENTS_PLACED / data.X_TOTAL_STUDENTS ) * 100
    data.target.fillna(0, inplace=True)
    data = data[['PROGRAMME', 'target']]
    programme_group = data.groupby('PROGRAMME')['target'].mean()
    programme_group.sort_values(ascending=False, inplace=True)

    trace = go.Bar(
        x = programme_group.index,
        y = programme_group
    )
    data = [trace]
    layout = go.Layout(
        title = "Average Target values in different programmes",
        yaxis = dict(
            title = "Target"
        ),
        xaxis = dict(
            title = "Programme Names"
        )
    )
    fig = go.Figure(data=data, layout= layout)
    print (tls.get_embed(py.plot(fig)))
