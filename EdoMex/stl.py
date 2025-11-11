import streamlit as st
import plotly.express as px
from func.db import obtain_data_by_casino
import numpy as np
import datetime
import pandas as pd

st.title("Satélite")
st.write("Ubicación de jugadores registrados en Satélite por nivel de jugador")

today = datetime.datetime.now()
date_range = st.date_input("Seleccionar rango de fechas", value=(datetime.date(2025, 1, 1), today))

if len(date_range) == 2:
    start_date, end_date = date_range
    df = obtain_data_by_casino('Satelite', start_date, end_date)
else:
    df = obtain_data_by_casino('Satelite')

if df.shape[0] == 0:
    st.subheader("Lo sentimos... no se encontró información")

else:
    df_plot = df.copy()

    # Aplica un pequeño desplazamiento (ajusta el valor según tu escala)
    df_plot["lat_jitter"] = df_plot["lat"] + np.random.uniform(-0.003, 0.003, len(df_plot))
    df_plot["lon_jitter"] = df_plot["lon"] + np.random.uniform(-0.003, 0.003, len(df_plot))

    df_casino_coor = pd.DataFrame({'lat_jitter': [19.502894053383294] , 'lon_jitter':[-99.2363873661102] , 'PLAYER_LEVEL_NAME': ['Casino Satelite']})

    df_plot = pd.concat([df_plot, df_casino_coor])
    fig = px.scatter_map(
        df_plot,
        lat="lat_jitter",
        lon="lon_jitter",
        color='PLAYER_LEVEL_NAME',
        hover_name='PLAYER_LEVEL_NAME'
    )
    fig.update_layout(
        autosize=False,
        height=700,
    )
    st.plotly_chart(fig)

    grouped = df.groupby("PLAYER_LEVEL_NAME").size().reset_index(name="Cantidad")
    cols = st.columns(len(grouped))

    for col, (nivel, cantidad) in zip(cols, grouped.itertuples(index=False)):
        col.metric(label=nivel, value=cantidad)


    st.divider()
    st.dataframe(df)