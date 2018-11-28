import pandas as pd
import os
import plotly
import plotly.offline as py2
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
plotly.tools.set_credentials_file(username='sominwadhwa', api_key='MPdahdMDsEvh11ffGZdB')
data1 = pd.read_csv("aicte1.csv")

Y = data1[['level', 'number_of_institutes']].groupby('level',as_index=False).sum()

trace0 = go.Bar(
    x = Y['level'],
    y = Y['number_of_institutes'],
    marker = dict(
        color = "#feda62"
    )
)

data = [trace0]

layout = go.Layout(
    title = "Institutes per Programme",
    titlefont = dict(
        size = '25'
    ),
    xaxis = dict(
        title = "Level",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Number of Institutes",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    # margin = dict(
    #     b = 500
    # )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'institutes_per_programme_bar', show_link = False)))
# py.plot(fig, filename = 'salary_distribution_bar.html', show_link=False)
# with open('salary_distribution_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
