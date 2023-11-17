import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.write('''
         # Controle de Fluxo de Pessoas - Smart Pixel
         
        ''')

cols = ["11/05", "14/05", "17/05", "20/05", "23/05", "26/05", "29/05", "01/06", "04/06", "07/06", "09/06"]
line = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

dados = random.randint(0, 2000)
df = pd.DataFrame(data=dados, index=line, columns=cols)

x = df.columns
y = df.index
plt.plot(x,y)

add_cameras = st.sidebar.selectbox(
    "Câmeras",
    ("Câmera 01", "Câmera 02", "Câmera 03")
)

if add_cameras == "Câmera 01":
    a01, b01, c01 = st.tabs(["Fluxo acumulado", "Fluxo de visitantes", "Tempo Real"])
    
    with a01:
        st.header("Fluxo acumulado obtido da câmera 01")
        st.pyplot(plt)

    with b01:
        st.header("Fluxo de visitantes obtido da câmera 01")
        st.pyplot(plt)
    
    with c01:
        st.header("Imagens em tempo real da câmera 01")
        st.video("video_modelo.mp4")


if add_cameras == "Câmera 02":
    a02, b02, c02 = st.tabs(["Fluxo acumulado", "Fluxo de visitantes", "Tempo Real"])

    with a02:
        st.header("Fluxo acumulado obtido da câmera 02")
        st.pyplot(plt)

    with b02:
        st.header("Fluxo de visitantes obtido da câmera 02")
        st.pyplot(plt)
    
    with c02:
        st.header("Imagens em tempo real da câmera 02")
        st.video("video_modelo.mp4")


if add_cameras == "Câmera 03":
    a03, b03, c03 = st.tabs(["Fluxo acumulado", "Fluxo de visitantes", "Tempo Real"])

    with a03:
        st.header("Fluxo acumulado obtido da câmera 03")
        st.pyplot(plt)

    with b03:
        st.header("Fluxo de visitantes obtido da câmera 03")
        st.pyplot(plt)
    
    with c03:
        st.header("Imagens em tempo real da câmera 03")
        st.video("video_modelo.mp4")