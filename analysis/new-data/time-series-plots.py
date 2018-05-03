import argparse
import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
plotly.__version__
import cufflinks as cf

import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
#plotly.offline.init_notebook_mode(connected=True)
import plotly.graph_objs as go


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-file", type="str")
    # args = parser.parse_args()
    # filename = args.file

    target_value = []
    target_value_mean = []
    files = ["1213", "1314", "1415", "1516", "1617"]
    for filename in files:
        temp = pd.read_csv(filename +".csv", encoding="latin1")
        new_columns = ['X_TOTAL_STUDENTS', 'NO_OF_STUDENTS_PLACED']
        temp = temp[new_columns]
        temp.fillna(0, inplace=True)
        temp = temp[temp.X_TOTAL_STUDENTS != 0]
        temp = temp[temp.NO_OF_STUDENTS_PLACED != 0]
        column_name = "target" + filename
        temp[filename] = (temp.NO_OF_STUDENTS_PLACED / temp.X_TOTAL_STUDENTS) * 100
        temp = temp[temp[filename] <=100]
        temp = temp[filename]
        target_value = target_value + [temp]
        target_value_mean = target_value_mean + [temp.mean()]

    print ("Distribution plot of percent of placed students in each year")
    fig = ff.create_distplot(target_value, ["2012", "2013", "2014", "2015", "2016"], show_hist=False, bin_size=0.1)
    plot(fig, show_link = False)

    print ("Line plot of average number of placed students from 2012 to 2016")
    layout = dict(title = 'Average number of placed students in the years 2012 to 2016',
              xaxis= dict(title= 'Years',ticklen= 5),
              yaxis= dict(title= 'Average Value',ticklen= 5),
              width = 800,
              height = 500
             )

    fig = dict(data = [go.Scatter(y=target_value_mean, x = ["2012", "2013", "2014", "2015", "2016"]
                              , mode = "lines+markers")], layout = layout)
    plot(fig)



if __name__ == "__main__":
    main()
