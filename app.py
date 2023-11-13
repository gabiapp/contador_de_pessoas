import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

st.write('''
         # Controle de Fluxo de Pessoas
         ## Smart Pixel
         ''')

cols = ["11/05", "14/05", "17/05", "20/05", "23/05", "26/05", "29/05", "01/06", "04/06", "07/06", "09/06"]
line = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

dados = random.randint(0, 2000)
df = pd.DataFrame(data=dados, index=line, columns=cols)

x = df.columns
y = df.index
plt.plot(x,y)


add_camera01 = st.sidebar.selectbox(
    "Câmera 01",
    ("Tempo real", "Fluxo acumulado", "Fluxo de visitantes"),
    key="camera01"
)

if add_camera01 == 'Tempo real':
    st.write("## Câmera 01 em tempo real")
    st.video("VIDEO - PESSOAS ANDANDO NA RUA HD.mp4")
elif add_camera01 == 'Fluxo acumulado':
    st.write("## Fluxo acumulado obtido pela câmera 01")
    st.pyplot(plt)
else:
    st.write("## Fluxo de visitantes obtido pela câmera 01")
    st.pyplot(plt)

    
add_camera02 = st.sidebar.selectbox(
    "Câmera 02",
    ("Tempo real", "Fluxo acumulado", "Fluxo de visitantes"),
    key="camera02"
)

if add_camera02 == 'Tempo real':
    st.write("## Câmera 02 em tempo real")
    st.video("VIDEO - PESSOAS ANDANDO NA RUA HD.mp4")
elif add_camera02 == 'Fluxo acumulado':
    st.write("## Fluxo acumulado obtido pela câmera 02")
    st.pyplot(plt)
else:
    st.write("## Fluxo de visitantes obtido pela câmera 02")
    st.pyplot(plt)

add_camera03 = st.sidebar.selectbox(
    "Câmera 03",
    ("Tempo real", "Fluxo acumulado", "Fluxo de visitantes"),
    key="camera03"
)

if add_camera03 == 'Tempo real':
    st.write("# Câmera 03 em tempo real")
    st.video("VIDEO - PESSOAS ANDANDO NA RUA HD.mp4")
elif add_camera03 == 'Fluxo acumulado':
    st.write(" ## Fluxo acumulado obtido pela câmera 03")
    st.pyplot(plt)
else:
    st.write(" ## Fluxo de visitantes obtido pela câmera 03")
    st.pyplot(plt)