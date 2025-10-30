import streamlit as st
import plotly.express as px
from func.db import obtain_data_by_casino

st.title("Neza")
st.write("Ubicación de jugadores registrados en Neza por nivel de jugador")

d = st.date_input("Seleccionar fecha de ultima visita de los usuarios", value=None)
if d:    
    df = obtain_data_by_casino('Neza', d)
else: 
    df = obtain_data_by_casino('Neza')
if df.shape[0] == 0:
    st.subheader("Lo sentimos... no se encontró información")

else:
        
    fig = px.scatter_map(df, lat="lat", lon="lon", color='PLAYER_LEVEL_NAME')
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