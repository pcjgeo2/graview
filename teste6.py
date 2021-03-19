import streamlit as st
from streamlit_folium import folium_static
import folium
from folium import IFrame
import pandas as pd
import requests
import random
import streamlit as st
from streamlit_folium import folium_static
import folium
import io

def random_html_color():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    return '#%02x%02x%02x' % (r, g, b)

def style_fcn(x):
    return { 'fillColor': random_html_color() }
st.image('http://www.ululante.com/GRAVIEW.JPG')
#for changing type of the maps
#add_select = st.sidebar.selectbox("What data do you want to see?",("OpenStreetMap", "Stamen Terrain","Stamen Toner"))

mapboxAccessToken = 'pk.eyJ1IjoicGNqZ2VvMiIsImEiOiJja2x3dnBta3AzNGh6MndwbTk5bnBtaWYwIn0.uz6reBxisN3YYfgJuCr8qg'

mapboxTilesetId = 'mapbox.satellite'

#url0 = ("http://www.ululante.com/")
#lb = f"{url0}/Fraturas.geojson"
#m = folium.Map(name="Satelite",location=[-5.268005,-37.967937], zoom_start=15, tiles='https://api.tiles.mapbox.com/v4/' + mapboxTilesetId + '/{z}/{x}/{y}.png?access_token=' + mapboxAccessToken,attr='mapbox.com')
m = folium.Map(location=[-1.717,-39.28], zoom_start=6, tiles="Stamen Terrain")


#folium.GeoJson('http://www.ululante.com/Limites_bacia.geojson', style_function=style_fcn,name="Limites Bacia").add_to(m)
#tooltip = "Liberty Bell"



bg='http://www.ululante.com/faults.png'
img = folium.raster_layers.ImageOverlay(name='faults',image=bg,bounds=[[-6.372, -45.407], [2.415, -31.387]],opacity=1,interactive=True,cross_origin=False,zindex=1,)
img.add_to(m)


bg='http://www.ululante.com/bouguer_residual_terraceado_lineamentos6.png'
img = folium.raster_layers.ImageOverlay(name='Bouguer Residual Terraceado',image=bg,bounds=[[-6.372, -45.407], [2.415, -31.387]],opacity=1,interactive=True,cross_origin=False,zindex=1,)
img.add_to(m)


#folium.GeoJson("Limites_bacia.geojson",style_function=style_fcn,name="Limites Bacia").add_to(m)
#folium.GeoJson("Fraturas.geojson",style_function=style_fcn,name="Fraturas Oceânicas").add_to(m)
#folium.GeoJson("blocos.geojson",style_function=style_fcn,name="Blocos").add_to(m)
#folium.GeoJson("campos.geojson",style_function=style_fcn,name="Campos").add_to(m)


style1 = {'fillColor': '#000000', 'color': '#000000'}
style2 = {'fillColor': '#FD2F03', 'color': '#FD2F03'}
style3 = {'fillColor': '#01FF12', 'color': '#01FF12'}
style4 = {'fillColor': '#FFFFFF', 'color': '#FFFFFF'}
folium.GeoJson("Limites_bacia.geojson",name="Limites Bacia",style_function=lambda x:style1).add_to(m)
folium.GeoJson("Fraturas.geojson",name="Fraturas Oceânicas",style_function=lambda x:style2,).add_to(m)
folium.GeoJson("blocos.geojson",name="Blocos",style_function=lambda x:style3).add_to(m)
folium.GeoJson("campos.geojson",name="Campos",style_function=lambda x:style4).add_to(m)









folium.LayerControl().add_to(m)
folium_static(m)