import streamlit as st
import plotly.express as px
from func.db import obtain_zip_code_players_shared

df = obtain_zip_code_players_shared('Estado de México')
st.title("Jugadores Compartidos en Estado de México")
st.write("Ubicación de jugadores compartidos entre los casinos del Estado de México")
fig = px.scatter_map(df, lat="lat", lon="lon", color='Casino')
fig.update_layout(
    autosize=False,
    height=700,
)
st.plotly_chart(fig)

grouped = df.groupby("Casino").size().reset_index(name="Cantidad")
cols = st.columns(len(grouped))

for col, (nivel, cantidad) in zip(cols, grouped.itertuples(index=False)):
    col.metric(label=nivel, value=cantidad)


st.divider()
st.dataframe(df)