# -*- coding: utf-8 -*-
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as graph_objs
import json
import csv
import numpy as np
import pandas as pd
import random
import plotly
import geocoder
plotly.tools.set_credentials_file(username='sharmaakshay', api_key='Q7PPhpMRXKFpL1SUnHm4')
with open('ind_geojson.json') as f:
    ind_geojson = json.load(f)

def getCityGeometry(city):
    # print ("to find: " + city.lower())
    city_geometry = {}
    city_geometry['type'] = 'FeatureCollection'
    city_geometry['features'] = []
    for feature in ind_geojson['features']:
        for i in range(1,4):
            # print (feature['properties']['NAME_' + str(i)].encode('utf-8').lower())
            if city.lower().strip() == feature['properties']['NAME_' + str(i)].lower().strip():
                city_geometry['features'].append(feature)
                # print ("found")
    return city_geometry

def getCoordinates(places):
    coordinates = {}
    for place in places:
        coordinates[place] = geocoder.google(place).latlng
        print ("got coordinates for " + place)
    return coordinates

# mapbox_access_token = 'pk.eyJ1IjoiYWRhbWt1bGlkamlhbiIsImEiOiJjaXNya29kemwwNDNoMnRtMXBobGtvbWE4In0._k_JKvR8MknvKmiUsJ6C7g'
mapbox_access_token = 'pk.eyJ1IjoiZGhydXZrdWNoaGFsIiwiYSI6ImNqMDVnanM5cTBsc3gzMnFyeHp2MGt5aHoifQ.dNvTWnEg5XXmy5bDAZq1Yw'

data = pd.read_csv("aicte1.csv")

data.head()

data1 = data.copy()
intake_difference = (data.intake - data.enrollment) / data.intake
intake_difference *= 100
data1 = data.copy()
data1['intake_difference'] = intake_difference
data1.loc[data1['intake_difference'] <= 0, 'intake_difference'] = 0
Y = data1[['state','intake_difference']].groupby('state',as_index=False).mean().sort('intake_difference',ascending=False)

print (Y)
# exit()
total = 0.0
city_opacity = {}
places_set = set(Y  ['state'])
city_coordinates = getCoordinates(places_set)
city_count = {}
max_opacity = -1

for index in Y.index.values:
    city_count[Y['state'][index]] = Y['intake_difference'][index]
    total += Y['intake_difference'][index]

print (city_count)
# exit()
# with open('cities_r2.csv', 'rb') as csvfile:
#     filereader = csv.DictReader(csvfile)
#     for row in filereader:
#         name_of_city = row['name_of_city'].strip()
#         total += int(row['population_total'])
#         city_count[name_of_city] = int(row['population_total'])
#         city_coordinates[name_of_city] = {"city_lat" : row['location'].split(',')[0], "city_lon": row['location'].split(',')[0]}

for city in city_count:
    city_opacity[city] = float(city_count[city]/total)
    if city_opacity[city] > max_opacity:
        max_opacity = city_opacity[city]

print ("max" + str(max_opacity))
for city in city_opacity:
    # city_opacity[city] += (0.80 - max_opacity)
    city_opacity[city] *= 10
    print (city  + ": "+ str(city_opacity[city]))


top_cities = []
i = 0
sorted_opacity_keys = sorted(city_opacity, key = city_opacity.get, reverse=True)

for city in sorted_opacity_keys:
    # print str(city_opacity[city])
    top_cities.append([city, str(round(city_count[city],2))])

data_text = []
data_lon = []
data_lat = []
layout_layers = []

# print city_count

for city in city_count:
    #data
    data_text.append(city.title() + " (" + str(round(city_count[city],2)) + ")")
    data_lon.append(city_coordinates[city][1])
    data_lat.append(city_coordinates[city][0])


    #layout
    layout_layers.append(
        dict(
            sourcetype = 'geojson',
            source = getCityGeometry(city),
            type = 'fill',
            # color = 'rgba(255,0,0,' + str(city_opacity[city]) + ')'
            color = '#ef5350',
            opacity = city_opacity[city]
        )
    )
    # print city
    # break

# print layout_layers
# print city_opacity
# raw_input()
print (data_lon)
print (data_lat)
print (data_text)
data = graph_objs.Data([
    graph_objs.Scattermapbox(
        lat = data_lat,
        lon = data_lon,
        mode = 'markers',
        text = data_text,
        marker = dict(
            # symbol = "cross",
            color = "#ef5350",
        )
    )
])
# print (layout_layers)
layout = graph_objs.Layout(
    title = "Intake Differences in India",
    height=600,
    width=500,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        layers = layout_layers,
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=20.553826,
            lon=80.878458
        ),
        zoom=3.2,
        style='streets'
    ),
    titlefont = dict(
        size = '27',
        color = "#000000"
    ),
    font = dict(
        size = '18',
        family = 'Roboto'
    ),
    # paper_bgcolor='#eeeeee',
    annotations=[
        dict(
            x=0,
            y=0,
            xref='x',
            yref='y',
            text="Source: wwww.aicte-india.org",
            showarrow=False,
        ),
        dict(
            # x=0 ,
            y=-.1,
            # xref ='x',
            yref ='y',
            xanchor = 'center',
            yanchor = 'bottom',
            text="<i>Highest differences in</i> :<br> <b>" +
            top_cities[0][0] + "</b> (" + top_cities[0][1] + "), followed by <b>" +
            top_cities[1][0] + "</b> (" + top_cities[1][1] + "), <b><br>" +
            top_cities[2][0] + "</b> (" + top_cities[2][1] + "), <b>" +
            top_cities[3][0] + "</b> (" + top_cities[3][1] + "), <b>" +
            top_cities[4][0] + "</b> (" + top_cities[4][1] + ")" ,
            showarrow = False,
            align = "center"
        )
    ]

)

fig = dict(data=data, layout=layout)
print("uploading map")
print (tls.get_embed(py.plot(fig, filename='aicte_intake_diff_map')))
