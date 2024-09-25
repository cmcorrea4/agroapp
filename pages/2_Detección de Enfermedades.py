import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

st.title("Detección de enfermedades")
st.write('Toma una fotografía de la hoja para detectar enfermedades.')

img_file_buffer = st.camera_input("Toma una Foto")
bg_image = st.file_uploader("Cargar Imagen:", type=["png", "jpg"])
if bg_image is not None:
    uploaded_file=bg_image
    st.image(uploaded_file, caption='Imagen cargada.', use_column_width=True)


if img_file_buffer is not None  or uploaded_file is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   #To read image file buffer as a PIL Image:
    img = Image.open(bg_image)   #img_file_buffer

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0]>0.5:
      st.header('Saludable, con Probabilidad: '+str( prediction[0][0]) )
    if prediction[0][1]>0.5:
      st.header('Con Semptoria, con Probabilidad: '+str( prediction[0][1]))

