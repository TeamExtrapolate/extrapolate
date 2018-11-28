import plotly
import plotly.plotly as py
import plotly.offline as py2
import plotly.tools as tls
from plotly.graph_objs import *
from plotly.grid_objs import Column, Grid
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='dhruvkuchhal', api_key='RDBg0usEFB6AYKwq9RDX')
# import datetime
# import numpy as np
# from IPython.display import Image

column_1 = Column(['SVM', 'Random Forest', 'Ridge Regression', 'Lasso Regression', 'Artificial Neural Network (MLP)'], 'Model')
column_2 = Column(['0.557180','0.501676', '0.495932', '0.505886', '0.530847'], 'RMSE (for normalized values of salary)') # Tabular data can be numbers, strings, or dates
grid = Grid([column_1, column_2])

layout = go.Layout(
    # title = "",
    # titlefont = dict(
    #     size = '25'
    # ),
    # font = dict(
    #     size = '18'
    # ),
    # xaxis = dict(
    #     title = "Level",
    #     # titlefont = dict(
    #     #     size = '24'
    #     # )
    # ),
    # yaxis = dict(
    #     title = "Placed",
    #     # titlefont = dict(
    #     #     size = '24'
    #     # )
    # ),
    # barmode='stack',

    font = dict(
        # size = "11",
        family = 'Raleway',
    ),
)

# fig = dict(data = data, layout = layout)
# print (tls.get_embed(py.plot(fig, filename = 'ml_rmse_table', show_link = False)))
#
url = py.grid_ops.upload(grid, filename='ml_rmse_table', world_readable=True, auto_open=True)
print(url)
