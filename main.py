import streamlit as st
st.set_page_config(layout="wide")

pages = {
    "Nuevo León": [
        st.Page("NuevoLeon/all.py", title="Allende"),
        st.Page("NuevoLeon/mty.py", title="Mitras"),
        st.Page("NuevoLeon/gpe.py", title="Guadalupe"),
        st.Page("NuevoLeon/snd.py", title="Sendero"),
        st.Page("NuevoLeon/jugadores_compartidos_nl.py", title="Jugadores Compartidos Nuevo León"),
    ],
    "Estado de México": [
        st.Page("EdoMex/esm.py", title="Esmeralda"),
        st.Page("EdoMex/nez.py", title="Neza"),
        st.Page("EdoMex/stl.py", title="Satelite"),
        st.Page("EdoMex/jugadores_compartidos_edomex.py", title="Jugadores Compartidos EdoMex"),
    ],
    "Guanajuato": [
        st.Page("Guanajuato/ira.py", title="Irapuato"),
    ],
    "Jalisco": [
        st.Page("Jalisco/ajj.py", title="Ajijic"),
    ]
}

pg = st.navigation(pages, position='top')
pg.run()