import streamlit as st
from PIL import Image

# [... resto del código anterior igual hasta la sección de tecnologías ...]

# Sección específica de beneficios
def show_benefits_section():
    st.markdown("### 🎯 Beneficios")
    
    # Crear columnas para organizar los beneficios
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: white; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                • Incremento en la productividad y eficiencia<br>
                • Reducción de pérdidas por enfermedades<br>
                • Optimización en el uso de recursos<br>
                • Mejor toma de decisiones basada en datos
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: white; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                • Agricultura más sostenible y precisa<br>
                • Recomendaciones personalizadas basadas en experiencia experta<br>
                • Acceso a conocimiento agrícola especializado<br>
                • Reducción de costos operativos
            </div>
        """, unsafe_allow_html=True)

def main():
    # [... código anterior del encabezado y características igual ...]

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
    
    # Llamar a la sección de beneficios
    show_benefits_section()

if __name__ == "__main__":
    main()
