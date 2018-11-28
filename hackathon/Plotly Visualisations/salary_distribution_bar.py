import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='sominwadhwa', api_key='MPdahdMDsEvh11ffGZdB')
dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

salary_distribution = data['Salary'].value_counts()

trace0 = go.Bar(
    x = salary_distribution.index.values,
    y = salary_distribution.values,
    marker = dict(
        color = "#83c185",
    )
)

data = [trace0]

layout = go.Layout(
    title = "Distribution of Salaries",
    titlefont = dict(size='25'),
    xaxis = dict(
        title = "Salary",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Frequency",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    font = dict(
        family = 'Raleway',
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'salary_distribution_bar', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'salary_distribution_bar.html', show_link=False)
# with open('salary_distribution_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
