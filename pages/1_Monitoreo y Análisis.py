import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image
from streamlit_lottie import st_lottie
import json

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Monitoreo IoT",
    page_icon="📊",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .header-style {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.7rem;
        margin-bottom: 2rem;
    }
    .subheader-style {
        background-color: #e8eaf6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .data-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.7rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .metric-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        margin: 0.5rem 0;
    }
    .chart-container {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .upload-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 0.7rem;
        margin: 1rem 0;
    }
    a {
        text-decoration: none;
        color: #0366d6;
        font-weight: 500;
    }
    a:hover {
        color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Encabezado Principal
    st.markdown("""
        <div class="header-style">
            <h1 style='text-align: center;'>📊 Monitoreo y Análisis de Datos</h1>
            <p style='text-align: center; font-size: 1.2em;'>Sistema Integral de Monitoreo Ambiental</p>
        </div>
    """, unsafe_allow_html=True)

    # Sección de Monitoreo Remoto
    st.markdown("""
        <div class="subheader-style">
            <h2>🌐 Monitoreo y Análisis Remoto</h2>
            <p>Monitorea en tiempo real las variables de temperatura y Humedad Relativa de tu sistema remoto.</p>
        </div>
    """, unsafe_allow_html=True)

    # Imagen y enlace en columnas
    col1, col2 = st.columns([2, 1])
    
    with col1:
        try:
            image = Image.open("IoT.jpg")
            new_image = image.resize((600, 400))
            st.image(new_image, caption="Sistema IoT de Monitoreo")
            with open('Experts.json') as source:
                 animation=json.load(source)
            st.lottie(animation,width =350)

        except Exception as e:
            st.error("Error al cargar la imagen del sistema")
    
    with col2:
        st.markdown("""
            <div style='padding: 2rem; background-color: #f8f9fa; border-radius: 0.5rem;'>
                <h3>📡 Acceso al Sistema</h3>
                <p>Accede al monitoreo en tiempo real a través del siguiente enlace:</p>
                <a href='http://157.230.214.127:8501/Monitoreo' target='_blank'>
                    🔗 Abrir Sistema de Monitoreo en Tiempo Real
                </a>
            </div>
        """, unsafe_allow_html=True)

    # Sección de Monitoreo Local
    st.markdown("""
        <div class="subheader-style">
            <h2>💻 Monitoreo y Análisis Local</h2>
            <p>Carga y analiza los datos obtenidos del sistema de monitoreo local.</p>
        </div>
    """, unsafe_allow_html=True)

    # Sección de carga de archivos
    with st.container():
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("📂 Selecciona el archivo con los datos de monitoreo")
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded_file is not None:
            try:
                # Procesamiento de datos
                column_names = ["Humedad", "Temperatura"]
                dataframe = pd.read_csv(uploaded_file, names=column_names)

                # Métricas básicas
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("""
                        <div class="metric-container">
                            <h4>📊 Total de Mediciones</h4>
                            <h2>{}</h2>
                        </div>
                    """.format(len(dataframe)), unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                        <div class="metric-container">
                            <h4>🌡️ Temperatura Promedio</h4>
                            <h2>{:.2f}°C</h2>
                        </div>
                    """.format(dataframe['Temperatura'].mean()), unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                        <div class="metric-container">
                            <h4>💧 Humedad Promedio</h4>
                            <h2>{:.2f}%</h2>
                        </div>
                    """.format(dataframe['Humedad'].mean()), unsafe_allow_html=True)

                # Configuración de tiempo
                st.markdown('<div class="data-container">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    d = st.date_input("📅 Fecha de inicio de la medición")
                with col2:
                    t = st.time_input("⏰ Hora de inicio de la medición")

                inicio = f"{d} {t}"
                indice_tiempo = pd.date_range(start=inicio, periods=len(dataframe), freq='2S')
                dataframe['Fecha'] = indice_tiempo
                dataframe = dataframe.set_index('Fecha')

                # Mostrar estadísticas
                st.markdown("<h3>📊 Estadísticas Básicas</h3>", unsafe_allow_html=True)
                st.dataframe(dataframe.describe())
                
                # Visualización de datos
                st.markdown("<h3>📈 Visualización de Datos</h3>", unsafe_allow_html=True)
                st.line_chart(dataframe)
                
                # Datos crudos
                with st.expander("Ver datos crudos"):
                    st.dataframe(dataframe)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error en el procesamiento de datos: {str(e)}")

if __name__ == "__main__":
    main()
