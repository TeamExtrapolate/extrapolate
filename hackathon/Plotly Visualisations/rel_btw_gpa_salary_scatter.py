import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='sharmaakshay', api_key='Q7PPhpMRXKFpL1SUnHm4')
dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

mean_salary = data.Salary.dropna().mean()
max_salary = data.Salary.dropna().max()
min_salary = data.Salary.dropna().min()
salary_data = data['Salary'].apply(lambda x: (x - mean_salary ) / (max_salary -min_salary ))

mean_gpa = data.collegeGPA.dropna().mean()
max_gpa = data.collegeGPA.dropna().max()
min_gpa = data.collegeGPA.dropna().min()
data['collegeGPA'] = data['collegeGPA'].apply(lambda x: (x - mean_gpa ) / (max_gpa -min_gpa ))

trace0 = go.Scatter(
    x = data['collegeGPA'],
    y = salary_data,
    mode = 'markers',
    marker = dict(
        color = "#f76664"
    )
)

data = [trace0]

layout = go.Layout(
    title = "Is Salary related to GPA?",
    font = dict(
        size = "11",
        family = 'Raleway',
    ),
    titlefont = dict(
        # color = '#8c9eac',
        size = '25'
    ),
    xaxis = dict(
        title = "College GPA",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Salary",
        # titlefont = dict(
        #     size = '24'
        # )
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig,filename = 'rel_btw_gpa_salary_scatter', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'rel_btw_gpa_salary_scatter.html', show_link = False)
# with open('rel_btw_gpa_salary_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
