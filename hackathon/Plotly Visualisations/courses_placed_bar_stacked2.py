import pandas as pd
import os
import plotly
import plotly.offline as py2
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')
data1 = pd.read_csv("aicte1.csv")

Z = data1[['level','placed']].groupby('level',as_index=False).sum()
Y = data1[['level', 'enrollment']].groupby('level',as_index=False).sum()
X = data1[['level', 'intake']].groupby('level',as_index=False).sum()

print (Z)
print (Y)
print (X)
# exit()

trace1 = go.Bar(
    x= Z['level'],
    y= Z['placed'],
    name='Placed',
    marker = dict(
        color = ["#59ae7f","#dc626f","#67537a"]
    ),
    hoverinfo = "none",
    # offset = 0,
)
trace2 = go.Bar(
    x=Z['level'],
    y= Y['enrollment'],
    # .sub(Z['placed']),
    name='Enrollment',
    marker = dict(
        color = ["#64c4af", "#ef9688", "#867198"]
    ),
    hoverinfo = "none",
    # offset = -0.5,
)
trace3 = go.Bar(
    x=Z['level'],
    y= X['intake'],
    # .sub(Y['enrollment']) ,
    name='Intake',
    marker = dict(
        color = ["#91ced7", "#ebcb94", "#aa99ba"]
    ),
    hoverinfo = "none",
    # offset = -0.5,
)
trace4 = go.Bar(
    offset = -0.5
)

data = [trace3, trace2, trace1, trace4]
layout = go.Layout(
    title = "Intake, Enrollment and Placement",
    titlefont = dict(
        size = '25'
    ),
    # font = dict(
    #     size = '18'
    # ),
    xaxis = dict(
        title = "Level",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Placed",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    barmode='group',

    font = dict(
        # size = "11",
        family = 'Raleway',
    ),
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py2.plot(fig, filename = 'courses_placed_bar_stacked', show_link = False)))
