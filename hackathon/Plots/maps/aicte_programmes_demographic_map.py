# -*- coding: utf-8 -*-
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as graph_objs
import json
import csv
import numpy as np
import geocoder
import pandas as pd
import random
import plotly
plotly.tools.set_credentials_file(username='sominwadhwa', api_key='MPdahdMDsEvh11ffGZdB')
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

data1 = pd.read_csv("aicte1.csv")
data_lev = pd.get_dummies(data1['level'])
data1 = data1.join(data_lev)
# data.head()

# data1 = data.copy()

# difference = (data.enrollment - data.placed) / data.enrollment
# difference = difference * 100
# data1 = data.copy()
# data1['difference'] = difference


# data1.loc[data1['difference'] <= 0, 'difference'] = 0

Z = data1[['DIPLOMA','UG','PG', 'state']].groupby('state',as_index=False).sum()
# print (Y)
# exit()
places_set = set(Z['state'])
coordinates = getCoordinates(places_set)

text_per_place = {}

for place in places_set:
    text = "Programmes :"
    # print (Z.loc[Z['place'] == place])
    filtered_Z = Z.loc[Z['state'] == place]
    print(filtered_Z)
    for index,row in filtered_Z.iterrows():
        text += "<br>"
        text += "DIPLOMA : "
        text += str(row['DIPLOMA'])
        text += "<br>UG : "
        text += str(row['UG'])
        text += "<br>PG : "
        text += str(row['PG'])
    text_per_place[place] = text

# print (text_per_place)
# print (Z.loc[Z['place'] == 'Andaman and Nicobar Islands'])
# exit()

total = 0.0
city_opacity = {}
# coordinates = {}
city_count = {}
max_opacity = -1

for index in Z.index.values:
    city_count[Z['state'][index]] = Z['DIPLOMA'][index] + Z['UG'][index] + Z['PG'][index]
    total += city_count[Z['state'][index]]

print (city_count)
# exit()
# with open('cities_r2.csv', 'rb') as csvfile:
#     filereader = csv.DictReader(csvfile)
#     for row in filereader:
#         name_of_city = row['name_of_city'].strip()
#         total += int(row['population_total'])
#         city_count[name_of_city] = int(row['population_total'])
#         coordinates[name_of_city] = {"city_lat" : row['location'].split(',')[0], "city_lon": row['location'].split(',')[0]}

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
    top_cities.append([city, str(city_count[city])])
data_text = []
data_lon = []
data_lat = []
layout_layers = []

# print city_count

for city in city_count:
    #data
    data_text.append(city.title() + "<br>" + text_per_place[city])
    data_lon.append(coordinates[city][1])
    data_lat.append(coordinates[city][0])


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
    title = "Distribution of programmes over India",
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
            text="<i>Highest number in</i> :<br> <b>" +
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
print (tls.get_embed(py.plot(fig, filename='aicte_programmes_demographic_map')))
