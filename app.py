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
    .benefits-list {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    .benefits-list p {
        margin: 0.5rem 0;
        padding-left: 1.5rem;
        position: relative;
    }
    .benefits-list p:before {
        content: "•";
        position: absolute;
        left: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
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
                    <ul>
                        <li>Temperatura y humedad en tiempo real</li>
                        <li>Análisis histórico de datos</li>
                        <li>Alertas y notificaciones personalizables</li>
                        <li>Visualización interactiva de datos</li>
                        <li>Informes automáticos y recomendaciones</li>
                    </ul>
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
                    <ul>
                        <li>Análisis de imágenes con IA</li>
                        <li>Detección temprana de patógenos</li>
                        <li>Identificación de Septoria y otras enfermedades</li>
                        <li>Recomendaciones de tratamiento</li>
                        <li>Historial de diagnósticos</li>
                    </ul>
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
                    <ul>
                        <li>Respuestas a consultas técnicas</li>
                        <li>Recomendaciones personalizadas</li>
                        <li>Base de conocimiento especializada</li>
                        <li>Soporte por voz y texto</li>
                        <li>Actualizaciones continuas de información</li>
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Sección de tecnologías y beneficios
    st.markdown("""
        <div class="tech-details">
            <h3>💡 Tecnologías Implementadas</h3>
            <p>Nuestros sistemas integran las últimas tecnologías de la Industria 4.0:</p>
            <ul>
                <li><strong>Internet de las Cosas (IoT):</strong> Sensores y dispositivos conectados para monitoreo en tiempo real</li>
                <li><strong>Inteligencia Artificial:</strong> Algoritmos avanzados para detección de enfermedades y análisis predictivo</li>
                <li><strong>Sistemas Expertos:</strong> Motores de inferencia para recomendaciones precisas basadas en conocimiento agrícola especializado</li>
                <li><strong>Big Data:</strong> Análisis de grandes volúmenes de datos para toma de decisiones informada</li>
                <li><strong>Computación en la Nube:</strong> Acceso a información y control desde cualquier lugar</li>
                <li><strong>Procesamiento de Lenguaje Natural:</strong> Interacción natural con el asistente virtual</li>
            </ul>
            
            <h3>🎯 Beneficios</h3>
            <div class="benefits-list">
                <p>Incremento en la productividad y eficiencia</p>
                <p>Reducción de pérdidas por enfermedades</p>
                <p>Optimización en el uso de recursos</p>
                <p>Mejor toma de decisiones basada en datos</p>
                <p>Agricultura más sostenible y precisa</p>
                <p>Recomendaciones personalizadas basadas en experiencia experta</p>
                <p>Acceso a conocimiento agrícola especializado</p>
                <p>Reducción de costos operativos</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
