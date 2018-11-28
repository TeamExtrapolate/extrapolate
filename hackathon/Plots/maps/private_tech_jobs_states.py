import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as graph_objs
import json
import csv

with open('ind_geojson.json') as f:
    ind_geojson = json.load(f)

def getStateGeometry(state):
    if state:
        state_geometry = {}
        state_geometry['type'] = 'FeatureCollection'
        state_geometry['features'] = []
        for feature in ind_geojson['features']:
            if state.lower() == feature['properties']['NAME_1'].encode('utf-8').lower():
                state_geometry['features'].append(feature)
        return state_geometry

def cityToState(city):
    for feature in ind_geojson['features']:
        for i in range(0,4):
            if city.lower() == feature['properties']['NAME_' + str(i)].encode('utf-8').lower():
                return feature['properties']['NAME_1']

# mapbox_access_token = 'pk.eyJ1IjoiYWRhbWt1bGlkamlhbiIsImEiOiJjaXNya29kemwwNDNoMnRtMXBobGtvbWE4In0._k_JKvR8MknvKmiUsJ6C7g'
mapbox_access_token = 'pk.eyJ1IjoiZGhydXZrdWNoaGFsIiwiYSI6ImNqMDVnanM5cTBsc3gzMnFyeHp2MGt5aHoifQ.dNvTWnEg5XXmy5bDAZq1Yw'

total = 0.0
city_opacity = {}
city_coordinates = {}
city_count = {}
max_opacity = -1
with open('ikdd_city_geo.csv', 'rb') as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        total += int(row['count'])
        city_count[row['JobCity']] = int(row['count'])
        city_coordinates[row['JobCity']] = {"city_lat" : row['city_lat'], "city_lon": row['city_lon']}

for city in city_count:
    city_opacity[city] = float(city_count[city]/total)
    if city_opacity[city] > max_opacity:
        max_opacity = city_opacity[city]

# print "max" + str(max_opacity)
for city in city_opacity:
    city_opacity[city] += (0.80 - max_opacity)
    # print city  + ": "+ str(city_opacity[city])

data_text = []
data_lon = []
data_lat = []
layout_layers = []

for city in city_coordinates:
    #data
    data_text.append(city.title() + " (" + str(city_count[city]) + ")")
    data_lon.append(city_coordinates[city]['city_lon'])
    data_lat.append(city_coordinates[city]['city_lat'])


    #layout
    layout_layers.append(
        dict(
            sourcetype = 'geojson',
            source = getStateGeometry(cityToState(city)),
            type = 'fill',
            # color = 'rgba(255,0,0,' + str(city_opacity[city]) + ')'
            color = 'rgb(255,0,0)',
            opacity = city_opacity[city]
        )
    )

data = graph_objs.Data([
    graph_objs.Scattermapbox(
        lat = data_lat,
        lon = data_lon,
        mode = 'markers',
        text = data_text
    )
])



layout = graph_objs.Layout(
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
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
py2.plot(fig, filename='private_tech_jobs')
