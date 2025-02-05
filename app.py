import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Tecnologías 4.0 para el Campo",
    page_icon="🌾",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .header-style {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 0.7rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    .content-section {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .section-title {
        color: #1f6feb;
        font-size: 24px;
        margin-bottom: 15px;
    }
    .feature-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Título y encabezado
st.markdown("""
    <div class="header-style">
        <h1>🌾 Aplicaciones Tecnológicas para el Campo</h1>
        <h2>MEJORA DE LA PRODUCTIVIDAD A TRAVÉS DEL USO DE TECNOLOGÍAS 4.0</h2>
    </div>
""", unsafe_allow_html=True)

# Imagen principal
try:
    image = Image.open("Agriculture.jpg")
    new_image = image.resize((1200, 400))
    st.image(new_image, caption="Tecnología para la Productividad", use_column_width=True)
except Exception as e:
    st.error("Error al cargar la imagen")

# Introducción
st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;'>
        <p style='font-size: 1.1em; line-height: 1.6;'>
            El uso de tecnologías de la Industria 4.0 permitirá mejorar las condiciones 
            de trabajo en el campo, la calidad de los productos y su productividad.
        </p>
    </div>
""", unsafe_allow_html=True)

# Sistemas disponibles
st.markdown("<h2 style='text-align: center; margin: 2rem 0;'>Nuestros Sistemas</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-box">
            <h3 style='color: #1f6feb; text-align: center;'>📊 Monitoreo y Análisis</h3>
            <p>Sistema de monitoreo ambiental:</p>
            • Seguimiento en tiempo real<br>
            • Análisis de datos históricos<br>
            • Alertas automáticas<br>
            • Reportes personalizados<br>
            • Visualización interactiva
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-box">
            <h3 style='color: #1f6feb; text-align: center;'>🔍 Detección de Enfermedades</h3>
            <p>Análisis de cultivos mediante IA:</p>
            • Detección temprana<br>
            • Identificación de patógenos<br>
            • Recomendaciones de tratamiento<br>
            • Seguimiento de evolución<br>
            • Base de datos de enfermedades
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-box">
            <h3 style='color: #1f6feb; text-align: center;'>🤖 Asistente Virtual</h3>
            <p>Consultor agrícola inteligente:</p>
            • Respuestas técnicas<br>
            • Consejos personalizados<br>
            • Soporte continuo<br>
            • Interacción por voz<br>
            • Actualización constante
        </div>
    """, unsafe_allow_html=True)

# Sección de tecnologías
st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;'>
        <h2 style='color: #1f6feb;'>💡 Tecnologías Implementadas</h2>
        <p style='margin-bottom: 15px;'>Nuestros sistemas integran las últimas tecnologías de la Industria 4.0:</p>
        
        <div style='background-color: white; padding: 20px; border-radius: 10px;'>
            • <b>Internet de las Cosas (IoT):</b> Sensores y dispositivos conectados para monitoreo en tiempo real<br><br>
            • <b>Inteligencia Artificial:</b> Algoritmos avanzados para detección de enfermedades y análisis predictivo<br><br>
            • <b>Sistemas Expertos:</b> Motores de inferencia para recomendaciones precisas basadas en conocimiento agrícola<br><br>
            • <b>Big Data:</b> Análisis de grandes volúmenes de datos para toma de decisiones informada<br><br>
            • <b>Computación en la Nube:</b> Acceso a información y control desde cualquier lugar<br><br>
            • <b>Procesamiento de Lenguaje Natural:</b> Interacción natural con el asistente virtual
        </div>
    </div>
""", unsafe_allow_html=True)

# Sección de beneficios
st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;'>
        <h2 style='color: #1f6feb;'>🎯 Beneficios</h2>
        
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>
            <div style='background-color: white; padding: 20px; border-radius: 10px;'>
                • Incremento en la productividad y eficiencia<br>
                • Reducción de pérdidas por enfermedades<br>
                • Optimización en el uso de recursos<br>
                • Mejor toma de decisiones basada en datos
            </div>
            
            <div style='background-color: white; padding: 20px; border-radius: 10px;'>
                • Agricultura más sostenible y precisa<br>
                • Recomendaciones personalizadas basadas en experiencia<br>
                • Acceso a conocimiento agrícola especializado<br>
                • Reducción de costos operativos
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
