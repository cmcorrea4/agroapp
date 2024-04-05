import streamlit as st
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image

st.title('Internet de las Cosas.')

#st.subheader("Internet de las Cosas")
image = Image.open("IoT.jpg")
st.write('Monitorea en tiempo real las variables de temperatura y Humedad Relativa.')
new_image = image.resize((600, 400))
st.image(new_image)

link_text = "[Monitoreo y Analisis de datos ](http://157.230.214.127:8501/Monitoreo)"

# Mostrar el hipervínculo utilizando st.markdown
st.markdown(link_text, unsafe_allow_html=True)
st.subheader('Recolección y análisis de datos.')
st.write('Carga aquí los datos obtenidos del sistema de toma de datos local.')
uploaded_file = st.file_uploader("Cargue el archivo con los datos.")
column_names=["Humedad","Temperatura"]
if uploaded_file is not None:
 
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, names=column_names)
  
    st.subheader('Estadisticos Básicos')
    st.write(dataframe.describe())
    st.write(len(dataframe))

    def generar_dataframe_con_timestamp(longitud):
      inicio = datetime.now()
      timestamps = [inicio + timedelta(seconds=i) for i in range(longitud)]
      df = pd.DataFrame(index=timestamps)
      return df
    #longitud_dataframe = 10
    #dataframe_con_timestamp = generar_dataframe_con_timestamp(longitud_dataframe)
    d = st.date_input("Fecha Inicio de la medición")
    t = st.time_input("Hora de Inicio de la medición")
    inicio = str(d)+" "+str(t) #datetime.now()
    st.write(inicio)
    indice_tiempo = pd.date_range(start=inicio, periods=len(dataframe), freq='2S')
    dataframe['Fecha'] =indice_tiempo
    dataframe = dataframe.set_index('Fecha')
    st.dataframe(dataframe)
    st.line_chart(dataframe)
