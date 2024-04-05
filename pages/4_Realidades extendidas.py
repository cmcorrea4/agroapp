import streamlit as st
from PIL import Image

st.title("Realidades extendidas")

st.write("Añadir a la realidad objetos digitales con Realidad Aumentada(AR), Construir Digitalmente cualquier espacio o elemento imaginado con realidad Virtual (VR).")

image = Image.open("Metaverso2.png")
new_image = image.resize((600, 400))
st.image(new_image)

link_text = "[Huertas Urbanas](https://www.spatial.io/s/Huertas-Urbanas-Expo-656b4f1541a07414005fd1f3?share=4171143912975730143)"
st.markdown(link_text, unsafe_allow_html=True)

image = Image.open("Metaverso.png")
new_image = image.resize((600, 400))
st.image(new_image)

link_text = "[Metaverso HUBTRADE](https://www.spatial.io/s/HUB-TRADE-2023-647d18b10551fa0adc8060c5?share=0)"
st.markdown(link_text, unsafe_allow_html=True)


#https://www.spatial.io/s/Huertas-Urbanas-Expo-656b4f1541a07414005fd1f3?share=4171143912975730143
