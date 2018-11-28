import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='prashasti', api_key='r55iCiSMro8stYszHC0g')

dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

salary = data.loc[:,['Salary','Designation']]
salary = salary.ix[salary['Designation']=='software engineer']
# print salary['Salary']
trace0 = go.Box(
    y = salary['Salary'],
    name = 'Salary',
    boxmean = 'sd',
    marker = dict(
        color = "#C5E1A5"
    )
    # fillcolor = '#eeeeee'
)

data = [trace0]

layout = go.Layout(
    title = "Underemployment",
    titlefont = dict(
        # size = '25',
        color = '#8c9eac'
        # color = "#000000"
    ),
    font = dict(
        # size = '18',
        family = 'Roboto',
        color = "#000000"
    ),
    # paper_bgcolor='#eeeeee',
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py2.plot(fig, filename = 'underemployment_box', show_link = False)))
# py2.plot(fig, filename = 'underemployment_box', show_link = False)
# print py2.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False)
# with open('underemployment_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
