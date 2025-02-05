import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Tecnologías 4.0 para el Campo",
    page_icon="🌾",
    layout="wide"
)

# Título principal
st.title('🌾 Aplicaciones Tecnológicas para el Campo')
st.header("MEJORA DE LA PRODUCTIVIDAD A TRAVÉS DEL USO DE TECNOLOGÍAS 4.0")

# Imagen principal
try:
    image = Image.open("Agriculture.jpg")
    new_image = image.resize((1200, 400))
    st.image(new_image, caption="Tecnología para la Productividad", use_column_width=True)
except Exception as e:
    st.error("Error al cargar la imagen")

# Texto introductorio
st.write('El uso de tecnologías de la Industria 4.0 permitirá mejorar las condiciones '
         'de trabajo en el campo, la calidad de los productos y su productividad.')

# Tecnologías Implementadas
st.subheader('💡 Tecnologías Implementadas')
st.write('Nuestros sistemas integran las últimas tecnologías de la Industria 4.0:')

with st.container():
    st.markdown("""
        * **Internet de las Cosas (IoT):** Sensores y dispositivos conectados para monitoreo en tiempo real
        * **Inteligencia Artificial:** Algoritmos avanzados para detección de enfermedades y análisis predictivo
        * **Sistemas Expertos:** Motores de inferencia para recomendaciones precisas basadas en conocimiento agrícola
        * **Big Data:** Análisis de grandes volúmenes de datos para toma de decisiones informada
        * **Computación en la Nube:** Acceso a información y control desde cualquier lugar
        * **Procesamiento de Lenguaje Natural:** Interacción natural con el asistente virtual
    """)

# Beneficios
st.subheader('🎯 Beneficios')

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        * Incremento en la productividad y eficiencia
        * Reducción de pérdidas por enfermedades
        * Optimización en el uso de recursos
        * Mejor toma de decisiones basada en datos
    """)

with col2:
    st.markdown("""
        * Agricultura más sostenible y precisa
        * Recomendaciones personalizadas basadas en experiencia
        * Acceso a conocimiento agrícola especializado
        * Reducción de costos operativos
    """)

# Sistemas Disponibles
st.subheader('🔧 Nuestros Sistemas')

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        ### 📊 Monitoreo y Análisis
        Sistema de monitoreo ambiental:
        * Seguimiento en tiempo real
        * Análisis de datos históricos
        * Alertas automáticas
        * Reportes personalizados
        * Visualización interactiva
    """)

with col2:
    st.markdown("""
        ### 🔍 Detección de Enfermedades
        Análisis de cultivos mediante IA:
        * Detección temprana
        * Identificación de patógenos
        * Recomendaciones de tratamiento
        * Seguimiento de evolución
        * Base de datos de enfermedades
    """)

with col3:
    st.markdown("""
        ### 🤖 Asistente Virtual
        Consultor agrícola inteligente:
        * Respuestas técnicas
        * Consejos personalizados
        * Soporte continuo
        * Interacción por voz
        * Actualización constante
    """)
