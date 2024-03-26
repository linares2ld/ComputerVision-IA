import cv2
import base64
import numpy as np

def decode(ruta):
    with open(ruta, 'r') as f: # Lee la imagen codificada desde el archivo de texto
        img_code = f.read()
    img_decode = base64.b64decode(img_code) # Decodifica la imagen desde base64
    img_numpy = np.frombuffer(img_decode, dtype=np.uint8) # Convierte los datos decodificados en un arreglo numpy

    return img_numpy

Lechuga = cv2.imdecode(decode('images/Lechuga.txt'), cv2.IMREAD_COLOR) # Lee la imagen con OpenCV
Lena = cv2.imdecode(decode('images/Lena.txt'), cv2.IMREAD_COLOR)
Rayas_verticales = cv2.imdecode(decode('images/Rayas_verticales.txt'), cv2.IMREAD_COLOR)
Tablero_ajedrez = cv2.imdecode(decode('images/Tablero_ajedrez.txt'), cv2.IMREAD_COLOR)