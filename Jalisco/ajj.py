import streamlit as st
import plotly.express as px
from func.db import obtain_data_by_casino
import numpy as np

st.title("Ajijic")
st.write("Ubicación de jugadores registrados en Ajijic por nivel de jugador")

d = st.date_input("Seleccionar fecha de ultima visita de los usuarios", value=None)
if d:    
    df = obtain_data_by_casino('Ajijic', d)
else: 
    df = obtain_data_by_casino('Ajijic')
if df.shape[0] == 0:
    st.subheader("Lo sentimos... no se encontró información")

else:
    df_plot = df.copy()

    # Aplica un pequeño desplazamiento (ajusta el valor según tu escala)
    df_plot["lat_jitter"] = df_plot["lat"] + np.random.uniform(-0.003, 0.003, len(df_plot))
    df_plot["lon_jitter"] = df_plot["lon"] + np.random.uniform(-0.003, 0.003, len(df_plot))

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