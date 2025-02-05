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
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 0.7rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    .feature-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.7rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        height: 100%;
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    .feature-title {
        color: #1f6feb;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .feature-description {
        color: #444;
        font-size: 1rem;
        line-height: 1.6;
    }
    .intro-text {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #444;
        margin: 2rem 0;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
    }
    .tech-details {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.7rem;
        margin: 1rem 0;
    }
    .benefits-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Principal
st.markdown("""
    <div class="header-style">
        <h1>🌾 Aplicaciones Tecnológicas para el Campo</h1>
        <h2>Mejora de la Productividad a través de Tecnologías 4.0</h2>
    </div>
""", unsafe_allow_html=True)

# Imagen principal
try:
    image = Image.open("Agriculture.jpg")
    new_image = image.resize((1200, 400))
    st.image(new_image, caption="Innovación Tecnológica en la Agricultura", use_column_width=True)
except Exception as e:
    st.error("Error al cargar la imagen principal")

# Texto introductorio
st.markdown("""
    <div class="intro-text">
        La integración de tecnologías de la Industria 4.0 en el sector agrícola representa una 
        revolución en la forma de trabajar el campo. Nuestras soluciones tecnológicas están 
        diseñadas para optimizar procesos, mejorar la calidad de los productos y aumentar 
        la productividad, todo mientras hacemos el trabajo agrícola más eficiente y sostenible.
    </div>
""", unsafe_allow_html=True)

# Sistemas disponibles
st.markdown("<h2 style='text-align: center; margin: 2rem 0;'>Nuestros Sistemas</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-container">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Sistema de Monitoreo y Análisis de Datos</div>
            <div class="feature-description">
                <p>Monitoreo en tiempo real de variables ambientales críticas para el cultivo:</p>
                • Temperatura y humedad en tiempo real<br>
                • Análisis histórico de datos<br>
                • Alertas y notificaciones personalizables<br>
                • Visualización interactiva de datos<br>
                • Informes automáticos y recomendaciones
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-container">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Detección de Enfermedades</div>
            <div class="feature-description">
                <p>Sistema inteligente de detección temprana de enfermedades en cultivos:</p>
                • Análisis de imágenes con IA<br>
                • Detección temprana de patógenos<br>
                • Identificación de Septoria y otras enfermedades<br>
                • Recomendaciones de tratamiento<br>
                • Historial de diagnósticos
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-container">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">Asistente Virtual Agrícola</div>
            <div class="feature-description">
                <p>Asistente inteligente para consultas y asesoramiento:</p>
                • Respuestas a consultas técnicas<br>
                • Recomendaciones personalizadas<br>
                • Base de conocimiento especializada<br>
                • Soporte por voz y texto<br>
                • Actualizaciones continuas de información
            </div>
        </div>
    """, unsafe_allow_html=True)

# Sección de tecnologías
st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;'>
        <h3>💡 Tecnologías Implementadas</h3>
        <p>Nuestros sistemas integran las últimas tecnologías de la Industria 4.0:</p>
        
        • <b>Internet de las Cosas (IoT):</b> Sensores y dispositivos conectados para monitoreo en tiempo real<br>
        • <b>Inteligencia Artificial:</b> Algoritmos avanzados para detección de enfermedades y análisis predictivo<br>
        • <b>Sistemas Expertos:</b> Motores de inferencia para recomendaciones precisas basadas en conocimiento agrícola especializado<br>
        • <b>Big Data:</b> Análisis de grandes volúmenes de datos para toma de decisiones informada<br>
        • <b>Computación en la Nube:</b> Acceso a información y control desde cualquier lugar<br>
        • <b>Procesamiento de Lenguaje Natural:</b> Interacción natural con el asistente virtual
    </div>
""", unsafe_allow_html=True)

# Sección de beneficios
st.markdown("### 🎯 Beneficios")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="benefits-box">
            • Incremento en la productividad y eficiencia<br>
            • Reducción de pérdidas por enfermedades<br>
            • Optimización en el uso de recursos<br>
            • Mejor toma de decisiones basada en datos
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="benefits-box">
            • Agricultura más sostenible y precisa<br>
            • Recomendaciones personalizadas basadas en experiencia experta<br>
            • Acceso a conocimiento agrícola especializado<br>
            • Reducción de costos operativos
        </div>
    """, unsafe_allow_html=True)
