import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Monitoreo IoT",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.3rem;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #0052a3;
    }
    .data-stats {
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .chart-container {
        padding: 1rem;
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .header-container {
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

def create_time_series_plot(df):
    """Crea un gráfico de series temporales con Plotly."""
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Temperatura a lo largo del tiempo', 'Humedad a lo largo del tiempo'),
        vertical_spacing=0.12
    )
    
    fig.add_trace(
        go.Scatter(x=df.index, y=df['Temperatura'], name='Temperatura', line=dict(color='#FF4B4B')),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=df.index, y=df['Humedad'], name='Humedad', line=dict(color='#2986cc')),
        row=2, col=1
    )
    
    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Monitoreo de Variables",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig

def main():
    # Header
    st.markdown("""
        <div class="header-container">
            <h1>📊 Sistema de Monitoreo y Análisis de Datos IoT</h1>
            <p>Plataforma integral para el monitoreo y análisis de variables ambientales en tiempo real</p>
        </div>
    """, unsafe_allow_html=True)

    # Crear dos columnas para la organización
    col1, col2 = st.columns([2, 1])

    with col1:
        # Imagen principal
        try:
            image = Image.open("IoT.jpg")
            new_image = image.resize((800, 400))
            st.image(new_image, caption="Sistema de Monitoreo IoT")
        except Exception as e:
            st.error("Error al cargar la imagen")

    with col2:
        st.markdown("""
            ### 🌡️ Características
            - Monitoreo en tiempo real
            - Análisis de datos históricos
            - Visualización interactiva
            - Alertas personalizables
            
            ### 🔗 Enlaces Rápidos
        """)
        st.markdown("[🔴 Monitoreo en Tiempo Real](http://157.230.214.127:8501/Monitoreo)")

    # Sección de carga de datos
    st.markdown("""
        <div class="header-container">
            <h2>📥 Análisis de Datos Históricos</h2>
            <p>Cargue sus datos históricos para un análisis detallado</p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Seleccione el archivo CSV con los datos históricos", type=['csv'])

    if uploaded_file is not None:
        try:
            # Carga y procesamiento de datos
            column_names = ["Humedad", "Temperatura"]
            dataframe = pd.read_csv(uploaded_file, names=column_names)
            
            # Configuración de la fecha y hora
            col1, col2 = st.columns(2)
            with col1:
                d = st.date_input("📅 Fecha de inicio de la medición")
            with col2:
                t = st.time_input("⏰ Hora de inicio de la medición")
            
            inicio = f"{d} {t}"
            indice_tiempo = pd.date_range(start=inicio, periods=len(dataframe), freq='2S')
            dataframe['Fecha'] = indice_tiempo
            dataframe = dataframe.set_index('Fecha')

            # Métricas principales
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown("""
                    <div class="metric-container">
                        <h3>🌡️ Temperatura Promedio</h3>
                        <h2>{:.2f}°C</h2>
                    </div>
                """.format(dataframe['Temperatura'].mean()), unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                    <div class="metric-container">
                        <h3>💧 Humedad Promedio</h3>
                        <h2>{:.2f}%</h2>
                    </div>
                """.format(dataframe['Humedad'].mean()), unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                    <div class="metric-container">
                        <h3>📊 Total Mediciones</h3>
                        <h2>{}</h2>
                    </div>
                """.format(len(dataframe)), unsafe_allow_html=True)
            
            with col4:
                st.markdown("""
                    <div class="metric-container">
                        <h3>⏱️ Duración</h3>
                        <h2>{}</h2>
                    </div>
                """.format(str(dataframe.index[-1] - dataframe.index[0]).split('.')[0]), unsafe_allow_html=True)

            # Estadísticas detalladas
            with st.expander("📊 Ver Estadísticas Detalladas"):
                st.markdown("<div class='data-stats'>", unsafe_allow_html=True)
                st.dataframe(dataframe.describe())
                st.markdown("</div>", unsafe_allow_html=True)

            # Visualización de datos
            st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
            fig = create_time_series_plot(dataframe)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # Datos raw
            with st.expander("📋 Ver Datos Crudos"):
                st.dataframe(dataframe)

        except Exception as e:
            st.error(f"Error al procesar los datos: {str(e)}")

if __name__ == "__main__":
    main()
