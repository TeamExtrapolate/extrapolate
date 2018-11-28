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

# print (Z)
# print (Y)
# print (X)
# exit()

x_enrollment = Y['level']
y_enrollment = Y['enrollment']
x_coord = [0,1,2]
# print(y_placed)
x_placed = Z['level']
y_placed = Z['placed']

x_intake = Z['level']
y_intake = X['intake']

annotation1=[
   dict(x=xi,y=yi+0.2,
        text='Enrollment',
        xanchor='auto',
        yanchor='bottom',
        showarrow=False,
        font = dict(
            family = "Raleway"
        )
   ) for xi, yi in zip(x_coord, y_enrollment)]

annotation2=[
   dict(x=xi+0.25,y=yi+0.2,
        text='Placed',
        xanchor='auto',
        yanchor='bottom',
        showarrow=False,
        font = dict(
            family = "Raleway"
        )
   ) for xi, yi in zip(x_coord, y_placed)]

annotation3=[
   dict(x=xi-0.25,y=yi+0.2,
        text='Intake',
        xanchor='auto',
        yanchor='bottom',
        showarrow=False,
        font = dict(
            family = "Raleway"
        )
   ) for xi, yi in zip(x_coord, y_intake)]

trace1 = go.Bar(
    x= Z['level'],
    y= Z['placed'],
    name='Placed',
    marker = dict(
        color = ["#1d628b","#f59500","#67537a"]
    ),
    # hoverinfo = "none",
    # offset = 3,
)
trace2 = go.Bar(
    x=Z['level'],
    y= Y['enrollment'],
    # .sub(Z['placed']),
    name='Enrollment',
    marker = dict(
        color = ["#4589b0", "#ffb836", "#867198"]
    ),
    # hoverinfo = "none",
    # offset = 3,
)
trace3 = go.Bar(
    x=Z['level'],
    y= X['intake'],
    # .sub(Y['enrollment']) ,
    name='Intake',
    marker = dict(
        color = ["#73b1d6", "#f4d35d", "#aa99ba"]
    ),
    # hoverinfo = "none",
    # offset = 3,
)

data = [trace3, trace2, trace1]
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
    annotations = annotation1  + annotation2 + annotation3

    #    dict(x=xi,y=yi,
    #         text=str(yi),
    #         xanchor='center',
    #         yanchor='top',
    #         showarrow=False,
    #    ) for xi, yi in zip(x_placed, y_placed),
    #    dict(x=xi,y=yi,
    #         text=str(yi),
    #         xanchor='center',
    #         yanchor='top',
    #         showarrow=False,
    #    ) for xi, yi in zip(x_placed, y_placed)
    #    dict(x=xi,y=yi,
    #         text=str(yi),
    #         xanchor='center',
    #         yanchor='top',
    #         showarrow=False,
    #    ) for xi, yi in zip(x_intake, y_intake)],
    #    dict(x=xi,y=yi,
    #         text=str(yi),
    #         xanchor='center',
    #         yanchor='top',
    #         showarrow=False,
    #    ) for xi, yi in zip(x_enrollment, y_enrollment)
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'courses_placed_bar_stacked', show_link = False)))
