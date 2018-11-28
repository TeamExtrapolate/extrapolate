import pandas as pd
import os
import plotly
import plotly.offline as py2
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

plotly.tools.set_credentials_file(username='aviralgupta', api_key='1gKSa84X3l2px8iQ5BRJ')

dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

job_cities = data['JobCity'].value_counts().head(10)
job_cities = job_cities.drop([-1]) #drop invalid index -1

trace0 = go.Pie(
    labels = job_cities.index.values,
    values = job_cities.values,
    marker = dict(
        colors = ["#83c185", "#FEDA62", "#83E3E2", "#60a9ce", "#C5E1A5", "#B39DDB", "#f76664", "#fff176", "#B0BEC5"],
        # line = dict(
        #     color = "#000000",
        #     width = "1"
        # )
    ),
    insidetextfont = dict(
        size = '11',
        # color = '#fff'
    ),
)

data = [trace0]

layout = go.Layout(
    title = "Jobs per City Distribution",
    # titlefont = dict(
    #     size = '48'
    # ),
    # font = dict(
    #     size = '18',
    #     family = 'Roboto'
    # ),
    # paper_bgcolor='#eeeeee',
    autosize = True,
    font = dict(
        size = "11",
        family = 'Raleway'
    ),
    titlefont = dict(
        # color = '#8c9eac',
        size = '25'
    ),
    legend = dict(
        orientation = 'h'
    )
    # margin = dict(
    #     r = 200
    # )

    # width = '919',
    # height = '700'
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'cities_max_jobs_pie', show_link = False, auto_open = False)))
# print tls.get_embed(py.plot(fig))
# with open('cities_max_jobs_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
