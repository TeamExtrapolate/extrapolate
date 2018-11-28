import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

def capitalize(x):
    return x.title()

dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)
salary_by_designation = data[['Designation','Salary']].groupby('Designation',as_index=False).mean().sort_values('Salary',ascending=False).head(10)

salary_by_designation['Designation'] = salary_by_designation['Designation'].apply(capitalize)


trace0 = go.Bar(
    x = salary_by_designation['Designation'],
    marker = dict(
        color = "#feda62"
    ),
    y = salary_by_designation['Salary'],
    
)

data = [trace0]

layout = go.Layout(
    title = "<br>Top 10 Highest Paying Jobs",
    titlefont = dict(
        size = '25',
        color = '#8c9eac'
        # color = "#000000"
    ),
    font = dict(
        size = '10',
        family = 'Roboto',
        color = "#000000"
    ),
    # paper_bgcolor='#eeeeee',
    xaxis = dict(
        title = "Designation",
        titlefont = dict(
            size = '18',
            color = '#8c9eac'
        )
    ),
    yaxis = dict(
        title = "Salary (in INR)",
        titlefont = dict(
            size = '18',
            color = '#8c9eac'
        )
    )
)

fig = dict(data = data, layout = layout)
py.plot(fig, filename = 'top_ten_highest_paying_jobs_bar',  show_link = False)
# print tls.get_embed(py.plot(fig, filename = 'top_ten_highest_paying_jobs_bar', link = False, show_link = False, auto_open = False))
# py.plot(fig, filename = 'top_ten_highest_paying_jobs_bar.html', show_link=False)
# with open('top_ten_highest_paying_jobs_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
