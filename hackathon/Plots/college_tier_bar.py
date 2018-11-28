from plotly import tools
import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')
def add_tier(x):
    return "Tier " + str(x)

dirname = os.path.dirname
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
data = pd.read_excel(path)

college_city_tier = data[['CollegeCityTier','Salary']].groupby('CollegeCityTier', as_index=False).mean()
college_tier = data[['CollegeTier','Salary']].groupby('CollegeTier', as_index=False).mean()

# print college_city_tier
# print college_tier

college_city_tier['CollegeCityTier'] = college_city_tier['CollegeCityTier'].apply(add_tier)
college_tier['CollegeTier'] = college_tier['CollegeTier'].apply(add_tier)

trace1 = go.Bar(
    # x = college_city_tier['CollegeCityTier'],
    x = ['Tier 1', 'Tier 2'],
    y = college_city_tier['Salary'],
    name = "College City Tier",
    # marker = dict(
    #     color = "#8bcdde"
    # )
)
trace2 = go.Bar(
    x = college_tier['CollegeTier'],
    y = college_tier['Salary'],
    name = "College Tier",
    # marker = dict(
    #     color = "#fd7150"
    # )
)
#subplot_titles = ('College City Tier', 'College Tier')
fig = tools.make_subplots(rows = 1, cols = 2, horizontal_spacing = 0.20, )
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(
    font = dict(
        # size = '18',
        family = 'Raleway'
    ),
)

fig['layout'].update(
    title = "College Tier and College City Tier",
    showlegend = False,
    # margin = dict(
    #     pad = 100
    # )
    titlefont = dict(size='25')
)

fig['layout']['xaxis2'].update(
    title = "College City Tier",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['yaxis2'].update(
    title = "Mean Salary",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['xaxis1'].update(
    title = "College Tier",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['yaxis1'].update(
    title = "Mean Salary",
    # titlefont = dict(
    #     size = '24'
    # )
)
print (tls.get_embed(py.plot(fig, filename = 'college_tier_bar', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'college_tier_bar.html', show_link=False)
# with open('college_tier_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
