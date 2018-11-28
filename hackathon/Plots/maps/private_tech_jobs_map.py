# -*- coding: utf-8 -*-
import plotly.offline as py2
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as graph_objs
import json
import csv
import plotly
plotly.tools.set_credentials_file(username='sominwadhwa', api_key='MPdahdMDsEvh11ffGZdB')
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

total = 0.0
city_opacity = {}
city_coordinates = {}
city_count = {}
max_opacity = -1
with open('ikdd_city_geo.csv', 'r') as csvfile:
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
    # city_opacity[city] += (0.80 - max_opacity)
    city_opacity[city] *= 1000
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
            source = getCityGeometry(city),
            type = 'fill',
            # color = 'rgba(255,0,0,' + str(city_opacity[city]) + ')'
            color = '#ef5350',
            opacity = city_opacity[city]
        )
    )

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

layout = graph_objs.Layout(
    title = "Distribution of<br>Private Sector Technology Jobs",
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
        # color = "#000000"
        # color = '#8c9eac'
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
            text="Source: AMEO 2015 | CoDS2016, IKDD",
            showarrow=False,
            font = dict(
                color = '#8c9eac',
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
            text="<i>Highest number of jobs in</i> :<br> <b>Bangalore</b> (687), followed by <b>Noida</b> (420) and <b>Hyderabad</b> (369)",
            showarrow = False,
            align = "center",
            font = dict(
                size = '11'
            )
        )
    ]

)

fig = dict(data=data, layout=layout)
print("Uploading graph now")
print (tls.get_embed(py.plot(fig, filename='private_tech_jobs')))
