import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='aviralgupta', api_key='1gKSa84X3l2px8iQ5BRJ')
dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

courses = data['Degree'].value_counts()

data = go.Pie(
    labels = courses.index.values,
    values = courses.values,
    marker = dict(
        colors = ["#f76664", "#FEDA62", "#83E3E2", "#60a9ce", "#C5E1A5", "#B39DDB", "#f76664", "#fff176", "#B0BEC5"],
        # line = dict(
        #     color = "#000000",
        #     width = "1"
        # )
    ),
    insidetextfont = dict(
        size = '15',
        # color = '#fff'
    ),
)

layout = go.Layout(
    title = "Technical Courses Distribution",
    titlefont = dict(
        size = '25'
    ),
    font = dict(
        size = '11',
        family = 'Raleway'
    ),
    # paper_bgcolor='#eeeeee',
    autosize = True,
    legend = dict(
        orientation = 'h'
    )
    # paper_bgcolor='#eeeeee',
)

fig = dict(data = [data], layout = layout)
# print tls.get_embed(py.plot(fig, filename = 'technical_courses_pie', show_link = False, auto_open = False))
print (tls.get_embed(py.plot(fig, filename = 'technical_courses_pie', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'technical_courses_pie.html', show_link = False)
# with open('technical_courses_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
