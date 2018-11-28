import pandas as pd
import os
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly
import pickle
plotly.tools.set_credentials_file(username='dhruvkuchhal', api_key='yUqN0qV3sFG4bMAfVjE1')
# dirname = os.path.dirname
# path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'train.xlsx')
# data = pd.read_excel(path)

# mean_salary = data.Salary.dropna().mean()
# max_salary = data.Salary.dropna().max()
# min_salary = data.Salary.dropna().min()
# salary_data = data['Salary'].apply(lambda x: (x - mean_salary ) / (max_salary -min_salary ))
#
# mean_gpa = data.collegeGPA.dropna().mean()
# max_gpa = data.collegeGPA.dropna().max()
# min_gpa = data.collegeGPA.dropna().min()
# data['collegeGPA'] = data['collegeGPA'].apply(lambda x: (x - mean_gpa ) / (max_gpa -min_gpa ))

pred = pickle.load(open('preds_plot.sav', 'rb'))

# print (pred)
# exit()


trace0 = go.Scatter(
    x = pred['Predicted'],
    y = pred['Difference'],
    mode = 'markers',
    marker = dict(
        color = "#f76664"
    )
)

data = [trace0]

layout = go.Layout(
    title = "Model Accuracy",
    # font = dict(
    #     size = "11"
    # ),
    titlefont = dict(
        # color = '#8c9eac',
        size = '25'
    ),
    xaxis = dict(
        title = "Predicted",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    yaxis = dict(
        title = "Difference",
        # titlefont = dict(
        #     size = '24'
        # )
    ),
    font = dict(
        family = "Raleway"
    )
)

fig = dict(data = data, layout = layout)
print (tls.get_embed(py.plot(fig,filename = 'residual_features_scatter', show_link = False, auto_open = False)))
# py.plot(fig, filename = 'rel_btw_gpa_salary_scatter.html', show_link = False)
# with open('rel_btw_gpa_salary_div.txt', 'w') as f:
#     f.write(py.plot(fig,include_plotlyjs=False, output_type = 'div', show_link = False))
