import streamlit as st
import streamlit_authenticator
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

from utils.preprocessing import Preprocessor

url = st.secrets['url_link']

@st.cache_data(ttl='1d',show_spinner=False)
def preprocessing(link_url):
    preprocessor = Preprocessor(link_url)
    preprocessor.apply_steps()
    df = preprocessor.df
    return df


df = preprocessing(url)

st.set_page_config(page_icon='./assets/phd.png',page_title='Panneaux')
st.header('Cartographie des panneaux du Bénin')

# Create the map
mapMod = folium.Map(location=(9.223351, 2.262477))

# Add the marker on the map
# add marker one by one on the map
for i in range(0,len(df)):
    html=f"""
        <h2> {df.iloc[i]['emplacement']}</h2>
        <h4> Description: </h4>
        {df.iloc[i]['format_panneau']}
        <h4> Nombre de faces: </h4>
        {df.iloc[i]['nombre_faces']}
        <h4> Image: </h4>
        <img src="{df.iloc[i]['lien_url']}"  width=200 height= 200>
        """
    iframe = folium.IFrame(html=html, width=230, height=230)
    popup = folium.Popup(iframe, max_width=2650)
    folium.CircleMarker(
        location=[df.iloc[i]['latitude'],df.iloc[i]['longitude']],popup=popup,
        #fill_color="#FFCA03",
        color="#09E6DA", opacity=.5, fill_opacity=.5, fill=True
        #icon=folium.Icon(color='gray',icon_color='#FFCA03')
    ).add_to(mapMod)

# Show the map again
mapMod.fit_bounds(mapMod.get_bounds())
st_data = st_folium(mapMod,width=700,height=500)