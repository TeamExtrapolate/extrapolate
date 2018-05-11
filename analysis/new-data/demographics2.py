from pymongo import MongoClient
import pandas as pd
import math
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as graph_objs
import json
import csv
import math
import plotly

plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')
mapbox_access_token = 'pk.eyJ1IjoiZGhydXZrdWNoaGFsIiwiYSI6ImNqMDVnanM5cTBsc3gzMnFyeHp2MGt5aHoifQ.dNvTWnEg5XXmy5bDAZq1Yw'

mongo = MongoClient('mongodb://elissa:readability@dhruvkuchhal.com:27017/advice_readability', connect = False)

db = mongo['advice_readability']

colors = ['#229954','#3498DB', '#E74C3C','#FFC300','#1ABC9C','#2E4053','#641E16','#1C2833','#6E2C00']

color_scheme = dict()
i = 0
for programme in db['aicte_data'].distinct('PROGRAMME'):
    color_scheme[programme] = colors[i]
    i += 1

def populate_db(CSV_FILE):
    df = pd.read_csv( CSV_FILE + ".csv",encoding = "ISO-8859-1")
    for i,row in df.iterrows():
        doc = dict()
        for column in df.columns:
            if (not (type(row[column]) is str)):
                if (not math.isnan(row[column])):
                    doc[column] = row[column]
            else:
                doc[column] = row[column]
        db['aicte_data'].update({'sno':doc['sno'],'ACADEMIC_YEAR':doc['ACADEMIC_YEAR']}, doc, upsert = True)
        print ('[' + CSV_FILE + '][' + str(i) + "] inserted into db...")

def getData(ACADEMIC_YEAR):
    data = list()

    # cnt = 0
    # total = len(db['aicte_data'].distinct('CURRENT_INSTITUTE_NAME', {'ACADEMIC_YEAR':ACADEMIC_YEAR}))
    for institute in db['aicte_data'].distinct('CURRENT_INSTITUTE_NAME', {'ACADEMIC_YEAR':ACADEMIC_YEAR}):
        doc = db['aicte_data'].find_one({'CURRENT_INSTITUTE_NAME':institute})
        
        datum = dict()
        
        if ('X_TOTAL_STUDENTS' in doc) and ('NO_OF_STUDENTS_PLACED' in doc):
            if (doc['X_TOTAL_STUDENTS'] > 0) and (doc['NO_OF_STUDENTS_PLACED'] > 0):
                datum['placed_ratio'] = doc['NO_OF_STUDENTS_PLACED']/doc['X_TOTAL_STUDENTS']
            else:
                continue
        else:
            continue
        
        datum['programme'] = doc['PROGRAMME'].title()
        geodoc = db['aicte_geocoder_results'].find_one({'place':doc['CURRENT_INSTITUTE_ADDRESS']})
        if (not geodoc) or (not geodoc['geocoder_result']):
            geodoc = db['aicte_geocoder_results'].find_one({'place':doc['INSTITUTE_DISTRICT'] + ', ' + doc['INSTI_STATE']})
            if (geodoc) and (not geodoc['geocoder_result']):
                continue
        if geodoc:
            datum['label'] = doc['CURRENT_INSTITUTE_NAME'].lower().title() + "<br>" + geodoc['geocoder_result']['address'].lower().title()
            datum['coordinates'] = (geodoc['geocoder_result']['lat'],geodoc['geocoder_result']['lng'])
            datum['color'] = color_scheme[doc['PROGRAMME']]
            data.append(datum)
        # print (str(cnt) + '/' + str(total))
        # cnt += 1
    
    return data

# for csv_filename in ['1213', '1314', '1415', '1516' ,'1617', '1718']:
#     populate_db(csv_filename)

def plot(data, ACADEMIC_YEAR):

    traces = list()
    # print (data)
    for datum in data:
        traces.append(
            graph_objs.Scattermapbox(
                lat = datum['coordinates'][0],
                lon = datum['coordinates'][1],
                text = datum['label'],
                mode = 'markers',
                opacity = datum['placed_ratio'],
                marker = graph_objs.Marker(
                    color = datum['color'],
                    size = 5
                ),
                name=datum['programme']
            )
        )
    
    # print (traces)
    # for color in colors:
    #     programme = None
    #     for programme_i in color_scheme:
    #         if color_scheme[programme_i] == color:
    #             if programme_i != "MCA":
    #                 programme_i = programme_i.title()
    #             programme = programme_i
    #             break
    #     lat = list()
    #     lng = list()
    #     text = list()
    #     for datum in data:
    #         if datum['color'] == color:
    #             lat.append(datum['coordinates'][0])
    #             lng.append(datum['coordinates'][1])
    #             text.append(datum['label'])
    #     traces.append(
    #         graph_objs.Scattermapbox(
    #             lat = lat,
    #             lon = lng,
    #             text = text,
    #             mode = 'markers',
    #             marker = graph_objs.Marker(
    #                 color = color,
    #                 size = 5
    #             ),
    #             name=programme
    #         )
    #     )

    layout = graph_objs.Layout(
        title = "Distribution of<br>Institutes in India",
        height=700,
        width=500,
        autosize=True,
        # showlegend = False,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=20.553826,
                lon=80.878458
            ),
            zoom=2.8,
            # zoom = 5,
            style='streets'
        ),
        titlefont = dict(
            size = '25',
            color = "#000000"
        ),
        font = dict(
            size = '18',
            family = 'Raleway'
        ),
        # paper_bgcolor='#eeeeee',
        # annotations=[
        #     dict(
        #         x=0,
        #         y=0,
        #         xref='x',
        #         yref='y',
        #         text="Source: AICTE Internal Database",
        #         showarrow=False,
        #         font = dict(
        #             size = '11'
        #         )
        #     ),
        # ]
    )

    fig = dict(data=graph_objs.Data(traces), layout=layout)
    print (ACADEMIC_YEAR)
    try:
        print (tls.get_embed(py.plot(fig, filename='institutes_demographics' + '_' + ACADEMIC_YEAR + '2')))
    except Exception as e:
        print (str(e))

ACADEMIC_YEARS_PROCESSED = ['2012-2013','2013-2014','2014-2015','2015-2016','2016-2017']

for ACADEMIC_YEAR in db['aicte_data'].distinct('ACADEMIC_YEAR'):
    # if ACADEMIC_YEAR in ACADEMIC_YEARS_PROCESSED:
    #     continue
    print("processing " + ACADEMIC_YEAR)
    plot(getData(ACADEMIC_YEAR), ACADEMIC_YEAR)
    # break