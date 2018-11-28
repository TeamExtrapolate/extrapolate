from plotly import tools
import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
import numpy as np
import pickle
plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')
# def add_tier(x):
#     return "Tier " + str(x)

# dirname = os.path.dirname
# path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
# data = pd.read_excel(path)

# college_city_tier = data[['CollegeCityTier','Salary']].groupby('CollegeCityTier', as_index=False).mean()
# college_tier = data[['CollegeTier','Salary']].groupby('CollegeTier', as_index=False).mean()

# print college_city_tier
# print college_tier

train = pickle.load(open('train.sav', 'rb'))
train.Salary = np.log1p(train.Salary)

salary = pickle.load(open('salary.sav', 'rb'))

#plot1
x_1 = list(set(salary))
y_1 = []

for value in x_1:
    y_1.append(list(salary).count(value))

# print (set(salary))

trace2 = go.Histogram(
    # x = college_city_tier['CollegeCityTier'],
    x = x_1,
    y = y_1,
    name = "Salary Distribution",
    nbinsx = 25
    # marker = dict(
    #     color = "#8bcdde"
    # )
)

#plot2
normalized_salary = np.log1p(salary)
x_2 = list(set(normalized_salary))
y_2 = []

for value in x_2:
    y_2.append(list(normalized_salary).count(value))
# exit()

# college_city_tier['CollegeCityTier'] = college_city_tier['CollegeCityTier'].apply(add_tier)
# college_tier['CollegeTier'] = college_tier['CollegeTier'].apply(add_tier)

trace1 = go.Histogram(
    x = x_2,
    y = y_2,
    name = "Normalized Salary",
    nbinsx = 25
    # marker = dict(
    #     color = "#fd7150"
    # )
)
#subplot_titles = ('College City Tier', 'College Tier')
fig = tools.make_subplots(rows = 1, cols = 2, horizontal_spacing = 0.20, )
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(
    # font = dict(
    #     size = '18'
    # )
)

fig['layout'].update(
    title = "Normalization of Salary",
    showlegend = False,
    # margin = dict(
    #     pad = 100
    # )
    titlefont = dict(size='25')
)

fig['layout']['xaxis2'].update(
    title = "Normalized Salary",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['yaxis2'].update(
    title = "Frequency",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['xaxis1'].update(
    title = "Salary",
    # titlefont = dict(
    #     size = '24'
    # )
)

fig['layout']['yaxis1'].update(
    title = "Frequency",
    # titlefont = dict(
    #     size = '24'
    # )
)
print (tls.get_embed(py.plot(fig, filename = 'salary_skewed_hist', show_link = False)))
# py.plot(fig, filename = 'college_tier_bar.html', show_link=False)
# with open('college_tier_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
