# -*- coding: utf-8 -*-
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as graph_objs
import json
import csv
import math
import plotly
plotly.tools.set_credentials_file(username='raunaq', api_key='y9L6p7Gkijuq8ptyjcS6')
colors = [
    '#5b2c6f',
    '#6c3483',
    '#7d3c98',
    '#8e44ad',
    '#a569bd',
    '#bb8fce'
]

with open('ind_geojson.json') as f:
    ind_geojson = json.load(f)

def getCityGeometry(city):
    # print "to find: " + city.lower()
    city_geometry = {}
    city_geometry['type'] = 'FeatureCollection'
    city_geometry['features'] = []
    for feature in ind_geojson['features']:
        for i in range(1,4):
            # print feature['properties']['NAME_' + str(i)].encode('utf-8').lower()
            if city.lower().strip() == feature['properties']['NAME_' + str(i)].strip().lower():
                city_geometry['features'].append(feature)
                # print "found"
    return city_geometry


# mapbox_access_token = 'pk.eyJ1IjoiYWRhbWt1bGlkamlhbiIsImEiOiJjaXNya29kemwwNDNoMnRtMXBobGtvbWE4In0._k_JKvR8MknvKmiUsJ6C7g'
mapbox_access_token = 'pk.eyJ1IjoiZGhydXZrdWNoaGFsIiwiYSI6ImNqMDVnanM5cTBsc3gzMnFyeHp2MGt5aHoifQ.dNvTWnEg5XXmy5bDAZq1Yw'

# total = 0.0
# total_graduates = 0.0
city_opacity = {}
city_coordinates = {}
city_count = {}
city_graduates_count = {}
max_opacity = -1
city_state = {}
with open('cities_r2.csv', 'r') as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        name_of_city = row['name_of_city'].strip()
        city_state[name_of_city] = row['state_name'].title()
        # total += int(row['population_total'])
        # total_graduates += int(row['total_graduates'])
        city_graduates_count[name_of_city] = float(row['total_graduates'])
        city_count[name_of_city] = float(row['population_total'])
        city_coordinates[name_of_city] = {"city_lat" : row['location'].split(',')[0], "city_lon": row['location'].split(',')[0]}

for city in city_count:
    # print "city_graduates_count[city]: " + str(city_graduates_count[city])
    # print "city_count[city] : " + str(city_count[city])
    city_opacity[city] = float(city_graduates_count[city]/city_count[city])
    if city_opacity[city] > max_opacity:
        max_opacity = city_opacity[city]

top_cities = []
i = 0
sorted_opacity_keys = sorted(city_opacity, key = city_opacity.get, reverse=True)

for city in sorted_opacity_keys:
    # print str(city_opacity[city])
    top_cities.append([city + ", " + city_state[city], str(round(city_opacity[city] * 100,2))])
    # i = i + 1
    # if (i == 3):
    #     break

# print "max" + str(max_opacity)
# for city in city_opacity:
    # city_opacity[city] += (0.80 - max_opacity)
    # city_opacity[city] /= 1.5
    # print city  + ": "+ str(city_opacity[city])

# exit()

def getColor(city):
    total = len(sorted_opacity_keys)
    print (colors[int((sorted_opacity_keys.index(city)*6)/total)])
    return colors[int((sorted_opacity_keys.index(city)*6)/total)]

def getOpacity(city):
    total = len(sorted_opacity_keys)
    n_elements_each_group = total/6.00
    opacity = (sorted_opacity_keys.index(city) % 6) / n_elements_each_group
    opacity *= 30
    print (opacity)
    return opacity

data_text = []
data_lon = []
data_lat = []
layout_layers = []

# print city_count

for city in city_coordinates:
    print(city)
    #data
    data_text.append(city.title() + " (" + str(city_count[city]) + ")")
    data_lon.append(city_coordinates[city]['city_lon'])
    data_lat.append(city_coordinates[city]['city_lat'])


    #layout
    layout_layers.append(
        dict(
            sourcetype = 'geojson',
            source = getCityGeometry(city),
            type = 'fill',
            # color = 'rgba(255,0,0,' + str(city_opacity[city]) + ')'
            color = getColor(city),
            opacity = getOpacity(city)
        )
    )
    # print city
    # break

# print (layout_layers)
# print city_opacity
# raw_input()



data = graph_objs.Data([
    graph_objs.Scattermapbox(
        # lat = data_lat,
        # lon = data_lon,
        # mode = 'markers',
        # text = data_text,
        # marker = dict(
        #     # symbol = "cross",
        #     color = "#ef5350",
        # )
    )
])

layout = graph_objs.Layout(
    title = "Distribution of<br>Number of Graduates in India",
    height=700,
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
        zoom=2.8,
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
    annotations=[
        dict(
            x=0,
            y=0,
            xref='x',
            yref='y',
            text="Source: Census, 2011 | Government of India",
            showarrow=False,
            font = dict(
                size = '11'
            )
        ),
        dict(
            # x=0 ,
            y=-.15,
            # xref ='x',
            yref ='y',
            xanchor = 'center',
            yanchor = 'bottom',
            text="<i>Highest percentage in</i> :<br> <b>" +
            top_cities[0][0] + "</b> (" + top_cities[0][1] + "%), followed by <b>" +
            top_cities[1][0] + "</b> (" + top_cities[1][1] + "%), <b><br>" +
            top_cities[2][0] + "</b> (" + top_cities[2][1] + "%), <b>" +
            top_cities[3][0] + "</b> (" + top_cities[3][1] + "%), <b>" +
            top_cities[4][0] + "</b> (" + top_cities[4][1] + "%)" ,
            showarrow = False,
            align = "center",
            font = dict(
                size = '11'
            )
        )
    ]

)

fig = dict(data=data, layout=layout)
print (tls.get_embed(py.plot(fig, filename='graduates_map')))
