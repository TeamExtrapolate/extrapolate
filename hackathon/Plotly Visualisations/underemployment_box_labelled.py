import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='dhruvkuchhal', api_key='yUqN0qV3sFG4bMAfVjE1')

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
        size = '25',
        # color = '#8c9eac'
        # color = "#000000"
    ),
    font = dict(
        # size = '18',
        family = 'Raleway',
        # color = "#000000"
    ),
    # annotations = [
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "3rd Quartile",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     "ay": -26.5,
    #     "borderwidth": 1,
    #     "ax": -94,
    #     "y": 400000,
    #     "x": -0.25,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   },
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "1st Quartile",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     "ay": 25.5,
    #     "borderwidth": 1,
    #     "ax": -97,
    #     "y": 252000,
    #     "x": -0.25,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   },
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "Median or 2nd Quartile",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     "ay": -11.5,
    #     "borderwidth": 1,
    #     "ax": 125,
    #     "y": 320000,
    #     "x": 0.25,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   },
    # #   {
    # #     "opacity": 1,
    # #     "bordercolor": "",
    # #     "xref": "x",
    # #     "arrowhead": 1,
    # #     "arrowsize": 1,
    # #     "yref": "y",
    # #     "text": "Outlier and Minimum value",
    # #     "align": "center",
    # #     "arrowwidth": 0,
    # #     "bgcolor": "rgba(0, 0, 0, 0)",
    # #     "ay": 1.5,
    # #     "borderwidth": 1,
    # #     "ax": -96,
    # #     "y": 1500000,
    # #     "x": 0,
    # #     "font": {
    # #       "color": "",
    # #       "family": "",
    # #       "size": 0
    # #     },
    # #     "borderpad": 1,
    # #     "arrowcolor": "",
    # #     "showarrow": True
    # #   },
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "Outlier and Maximum value",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     "ay": -10.5,
    #     "borderwidth": 1,
    #     "ax": 97,
    #     "y": 1500000,
    #     "x": 0.0171875,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   },
    # #   {
    # #     "opacity": 1,
    # #     "bordercolor": "",
    # #     "xref": "x",
    # #     "arrowhead": 1,
    # #     "arrowsize": 1,
    # #     "yref": "y",
    # #     "text": "Outlier",
    # #     "align": "center",
    # #     "arrowwidth": 0,
    # #     "bgcolor": "rgba(0, 0, 0, 0)",
    # #     "ay": 8.5,
    # #     "borderwidth": 1,
    # #     "ax": 62,
    # #     "y": 77.65883695346756,
    # #     "x": 0.016007698267981322,
    # #     "font": {
    # #       "color": "",
    # #       "family": "",
    # #       "size": 0
    # #     },
    # #     "borderpad": 1,
    # #     "arrowcolor": "",
    # #     "showarrow": True
    # #   },
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "Upper whisker - Maximum value that is not an outlier",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     "ay": -24.5,
    #     "borderwidth": 1,
    #     "ax": 136,
    #     "y": 620000,
    #     "x": 0.125,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   },
    # {
    #   "opacity": 1,
    #   "bordercolor": "",
    #   "xref": "x",
    #   "arrowhead": 1,
    #   "arrowsize": 1,
    #   "yref": "y",
    #   "text": "3rd Quartile + 1.5 (Inter Quartile Range)",
    #   "align": "center",
    #   "arrowwidth": 0,
    #   "bgcolor": "rgba(0, 0, 0, 0)",
    # #   "ay": -24.5,
    #   "borderwidth": 1,
    # #   "ax": 136,
    #   "ay": -26.5,
    #   "ax": -94,
    #   "y": 620000,
    #   "x": -0.125,
    #   "font": {
    #     "color": "",
    #     "family": "",
    #     "size": 0
    #   },
    #   "borderpad": 1,
    #   "arrowcolor": "",
    #   "showarrow": True
    # },
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "Lower whisker - Minimum value that is not an outlier",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     "ay": -44.5,
    #     "borderwidth": 1,
    #     "ax": 116,
    #     "y": 60000,
    #     "x": 0.125,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   },
    #   {
    #     "opacity": 1,
    #     "bordercolor": "",
    #     "xref": "x",
    #     "arrowhead": 1,
    #     "arrowsize": 1,
    #     "yref": "y",
    #     "text": "1st Quartile - 1.5 (Inter Quartile Range)",
    #     "align": "center",
    #     "arrowwidth": 0,
    #     "bgcolor": "rgba(0, 0, 0, 0)",
    #     # "ay": -44.5,
    #     "borderwidth": 1,
    #     # "ax": 116,
    #     "ay": -26.5,
    #     "ax": -94,
    #     "y": 60000,
    #     "x": -0.125,
    #     "font": {
    #       "color": "",
    #       "family": "",
    #       "size": 0
    #     },
    #     "borderpad": 1,
    #     "arrowcolor": "",
    #     "showarrow": True
    #   }
    # ],
    autosize = True
    # paper_bgcolor='#eeeeee',
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'underemployment_box', show_link = False)))
# py2.plot(fig, filename = 'underemployment_box', show_link = False)
# print py2.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False)
# with open('underemployment_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
