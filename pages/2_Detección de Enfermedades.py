import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
import logging
from streamlit_lottie import st_lottie
import json

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Detección de Enfermedades en Plantas",
    page_icon="🌿",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .success-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
    }
    .warning-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        color: #856404;
    }
    </style>
    """, unsafe_allow_html=True)

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DiseaseDetector:
    def __init__(self, model_path='keras_model.h5'):
        """Inicializa el detector de enfermedades."""
        self.model = self.load_model(model_path)
        self.image_size = (224, 224)
        self.input_shape = (1, 224, 224, 3)
        
    @staticmethod
    def load_model(model_path):
        """Carga el modelo de manera segura."""
        try:
            return load_model(model_path)
        except Exception as e:
            logger.error(f"Error al cargar el modelo: {e}")
            st.error("Error al cargar el modelo. Por favor, verifique que el archivo del modelo existe.")
            return None

    def preprocess_image(self, image_data):
        """Preprocesa la imagen para la predicción."""
        try:
            # Convertir a imagen PIL si es necesario
            if not isinstance(image_data, Image.Image):
                image = Image.open(image_data)
            else:
                image = image_data
            
            # Asegurar que la imagen está en modo RGB
            if image.mode != "RGB":
                image = image.convert("RGB")
            
            # Redimensionar
            image = image.resize(self.image_size)
            
            # Convertir a array y normalizar
            img_array = np.array(image)
            normalized_array = (img_array.astype(np.float32) / 127.0) - 1
            
            return np.reshape(normalized_array, self.input_shape)
            
        except Exception as e:
            logger.error(f"Error en el preprocesamiento: {e}")
            st.error("Error al procesar la imagen. Por favor, intente con otra imagen.")
            return None

    def predict(self, image_data):
        """Realiza la predicción sobre la imagen procesada."""
        try:
            if self.model is None:
                return None
                
            processed_image = self.preprocess_image(image_data)
            if processed_image is None:
                return None
                
            return self.model.predict(processed_image)
            
        except Exception as e:
            logger.error(f"Error en la predicción: {e}")
            st.error("Error al realizar la predicción. Por favor, intente nuevamente.")
            return None

def main():
    # Título y descripción
    st.title("🌿 Sistema de Detección de Enfermedades en Plantas")
    st.markdown("""
        Este sistema utiliza inteligencia artificial para detectar enfermedades en plantas 
        a través del análisis de imágenes. Puede cargar una imagen o tomar una foto con su cámara.
    """)
    with open('scan.json') as source:
         animation=json.load(source)
    st.lottie(animation,width =350)
    
    # Inicializar el detector
    detector = DiseaseDetector()
    
    # Crear columnas para la interfaz
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Método de Captura de Imagen")
        method = st.radio(
            "Seleccione el método de entrada:",
            ["Cámara", "Cargar Archivo"],
            key="capture_method"
        )

    # Procesar entrada según el método seleccionado
    image_data = None
    
    if method == "Cámara":
        image_data = st.camera_input("Tomar Foto")
    else:
        image_data = st.file_uploader("Cargar Imagen", type=["jpg", "jpeg", "png"])

    # Procesar la imagen si existe
    if image_data is not None:
        with st.spinner('Procesando imagen...'):
            # Mostrar la imagen
            st.image(image_data, caption="Imagen a analizar", use_column_width=True)
            
            # Realizar predicción
            prediction = detector.predict(image_data)
            
            if prediction is not None:
                st.subheader("📊 Resultados del Análisis")
                
                # Mostrar resultados
                col1, col2 = st.columns(2)
                
                with col1:
                    if prediction[0][0] > 0.5:
                        probability = f"{prediction[0][0]*100:.2f}%"
                        st.markdown(f"""
                            <div class='success-message'>
                                <h3>✅ Planta Saludable</h3>
                                <p>Probabilidad: {probability}</p>
                            </div>
                        """, unsafe_allow_html=True)
                    
                with col2:
                    if prediction[0][1] > 0.5:
                        probability = f"{prediction[0][1]*100:.2f}%"
                        st.markdown(f"""
                            <div class='warning-message'>
                                <h3>⚠️ Septoria Detectada</h3>
                                <p>Probabilidad: {probability}</p>
                            </div>
                        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
