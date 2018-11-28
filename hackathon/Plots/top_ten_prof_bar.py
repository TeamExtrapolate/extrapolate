import pandas as pd
import os
import plotly
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='prashasti', api_key='r55iCiSMro8stYszHC0g')


def capitalize(x):
    return x.title()

dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)
salary_by_designation = data[['Designation','Salary']].groupby('Designation',as_index=False).mean().sort_values('Salary',ascending=False).head(10)
data['Designation'] = data['Designation'].apply(capitalize)
profession = data['Designation'].value_counts().head(10)

trace0 = go.Bar(
    x = profession.index.values,
    y = profession.values,
    marker = dict(
        color = "#feda62"
    )
)

data = [trace0]

layout = go.Layout(
    title = "Top 10 Technology Professions",
    font = dict(
        size = "8",
        family = 'Raleway'
    ),
    titlefont = dict(
        # color = '#8c9eac',
        size = '25'
    ),
    xaxis = dict(
        title = "Designation",
        # titlefont = dict(
        #     # color = '#8c9eac',
        #     size = '18'
        # )
    ),
    yaxis = dict(
        title = "Frequency",
        # titlefont = dict(
        #     # color = '#8c9eac',
        #     size = '18'
        # )
    ),
    margin = dict(
        b = 100,
        # pad = 50
    ),
    # font = dict(
    #     size = '11',
    #     family = 'Raleway'
    # ),
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig, filename = 'top_ten_professions_bar', show_link = False)))
# py.plot(fig, filename = 'top_ten_professions_bar.html', show_link=False)
# with open('most_common_prof_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
