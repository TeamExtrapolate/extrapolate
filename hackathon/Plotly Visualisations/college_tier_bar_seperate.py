from plotly import tools
import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

def add_tier(x):
    return "Tier " + str(x)

dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

college_city_tier = data[['CollegeCityTier','Salary']].groupby('CollegeCityTier', as_index=False).mean()
college_tier = data[['CollegeTier','Salary']].groupby('CollegeTier', as_index=False).mean()


college_city_tier['CollegeCityTier'] = college_city_tier['CollegeCityTier'].apply(add_tier)
college_tier['CollegeTier'] = college_tier['CollegeTier'].apply(add_tier)

trace1 = go.Bar(
    x = college_city_tier['CollegeCityTier'],
    y = college_city_tier['Salary'],
    name = "College City Tier"
)
trace2 = go.Bar(
    x = college_tier['CollegeTier'],
    y = college_tier['Salary'],
    name = "College Tier"
)

data = [trace1]

layout = go.Layout(
    title = "College City Tier",
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
        title = "College City Tier",
        titlefont = dict(
            size = '18',
            color = '#8c9eac'
        )
    ),
    yaxis = dict(
        title = "Mean Salary (in INR)",
        titlefont = dict(
            size = '18',
            color = '#8c9eac'
        )
    )
)

fig = dict(data = data, layout = layout)

print (tls.get_embed(py.plot(fig, filename = 'college_city_tier_bar', show_link = False, auto_open = False)))

data = [trace2]

layout = go.Layout(
    title = "College Tier",
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
        title = "College Tier",
        titlefont = dict(
            size = '18',
            color = '#8c9eac'
        )
    ),
    yaxis = dict(
        title = "Mean Salary (in INR)",
        titlefont = dict(
            size = '18',
            color = '#8c9eac'
        )
    )
)

fig = dict(data = data, layout = layout)

print (tls.get_embed(py.plot(fig, filename = 'college_tier_bar', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'college_tier_bar.html', show_link=False)
# with open('college_tier_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
