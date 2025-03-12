import streamlit as st
import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from PIL import Image
import glob
from gtts import gTTS
import os
import time
import logging
from pathlib import Path
from streamlit_lottie import st_lottie
import json

# Configuración de la página
st.set_page_config(
    page_title="Sistema Experto Agrícola",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuración de estilos
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.3rem;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .api-input {
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
    }
    .success-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        margin: 1rem 0;
    }
    .error-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        color: #721c24;
        margin: 1rem 0;
    }
    .sidebar {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExpertSystem:
    def __init__(self):
        self.temp_dir = Path("temp")
        self.temp_dir.mkdir(exist_ok=True)
        self.pdf_path = "Septoria.pdf"
        
    def setup_openai(self, api_key):
        """Configura la API key de OpenAI."""
        os.environ['OPENAI_API_KEY'] = api_key
        
    def load_pdf(self):
        """Carga y procesa el archivo PDF."""
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            logger.error(f"Error al cargar el PDF: {e}")
            return None
            
    def create_knowledge_base(self, text):
        """Crea la base de conocimiento a partir del texto."""
        try:
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=500,
                chunk_overlap=20,
                length_function=len
            )
            chunks = text_splitter.split_text(text)
            embeddings = OpenAIEmbeddings()
            return FAISS.from_texts(chunks, embeddings)
        except Exception as e:
            logger.error(f"Error al crear la base de conocimiento: {e}")
            return None
            
    def generate_audio(self, text):
        """Genera el audio a partir del texto."""
        try:
            tts = gTTS(text, lang="es", tld="es", slow=False)
            filename = f"temp/audio_{int(time.time())}.mp3"
            tts.save(filename)
            return filename
        except Exception as e:
            logger.error(f"Error al generar el audio: {e}")
            return None
            
    def cleanup_old_files(self, days=7):
        """Limpia archivos temporales antiguos."""
        try:
            now = time.time()
            for file in self.temp_dir.glob("*.mp3"):
                if file.stat().st_mtime < now - (days * 86400):
                    file.unlink()
                    logger.info(f"Archivo eliminado: {file}")
        except Exception as e:
            logger.error(f"Error al limpiar archivos: {e}")

def main():
    # Inicialización del sistema
    expert_system = ExpertSystem()
    
    # Sidebar con información
    with st.sidebar:
        st.title("ℹ️ Información")
        st.markdown("""
        Este sistema experto utiliza inteligencia artificial para responder 
        preguntas sobre el cultivo y enfermedades de plantas.
        
        ### Características:
        - 🤖 IA Avanzada
        - 🗣️ Respuestas por voz
        - 📚 Base de conocimiento especializada
        
        ### Instrucciones:
        1. Ingrese su clave API de OpenAI
        2. Formule su pregunta
        3. Opcionalmente, escuche la respuesta
        """)

    # Contenido principal
    st.title('🌿 Sistema Experto Agrícola')
    
    # Cargar y mostrar imagen
    try:
        #image = Image.open('assitant_farm.jpg')
        #st.image(image, width=600, caption="Asistente Agrícola Virtual")
        with open('farmer.json') as source:
             animation=json.load(source)
        st.lottie(animation,width =450)
    except Exception as e:
        logger.error(f"Error al cargar la imagen: {e}")
    
    # Input de API Key con diseño mejorado
    st.markdown("<div class='api-input'>", unsafe_allow_html=True)
    api_key = st.text_input('🔑 Ingrese su clave:', type='password')
    st.markdown("</div>", unsafe_allow_html=True)
    
    if api_key:
        expert_system.setup_openai(api_key)
        
        # Cargar y procesar PDF
        text = expert_system.load_pdf()
        if text:
            knowledge_base = expert_system.create_knowledge_base(text)
            
            if knowledge_base:
                # Área de preguntas
                st.subheader("💭 ¿Qué deseas consultar?")
                user_question = st.text_input("", placeholder="Escribe tu pregunta aquí...")
                
                if user_question:
                    with st.spinner('Analizando tu pregunta...'):
                        try:
                            docs = knowledge_base.similarity_search(user_question)
                            llm = OpenAI(model_name="gpt-4")
                            chain = load_qa_chain(llm, chain_type="stuff")
                            
                            with get_openai_callback() as cb:
                                response = chain.run(input_documents=docs, question=user_question)
                            
                            # Mostrar respuesta con formato
                            st.markdown("<div class='success-message'>", unsafe_allow_html=True)
                            st.markdown("### 📝 Respuesta:")
                            st.write(response)
                            st.markdown("</div>", unsafe_allow_html=True)
                            
                            # Opción de audio
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                if st.button("🔊 Escuchar"):
                                    audio_file = expert_system.generate_audio(response)
                                    if audio_file:
                                        with open(audio_file, "rb") as f:
                                            st.audio(f.read(), format="audio/mp3")
                                            
                        except Exception as e:
                            st.error(f"Ocurrió un error al procesar tu pregunta. Por favor, intenta nuevamente.")
                            logger.error(f"Error en el procesamiento: {e}")
    
    # Limpieza automática de archivos
    expert_system.cleanup_old_files()

if __name__ == "__main__":
    main()

