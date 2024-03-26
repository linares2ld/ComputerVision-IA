import cv2
import base64

def code_png(ruta,nombre):
    img = cv2.imread(ruta) # Lee la imagen
    img_code = base64.b64encode(cv2.imencode('.png', img)[1]).decode() # Codifica la imagen en base64

    with open(f'{nombre}.txt', 'w') as f: # Guarda la imagen codificada en un archivo de texto
        f.write(img_code)

def code_jpg(ruta,nombre):
    img = cv2.imread(ruta) # Lee la imagen
    img_code = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode() # Codifica la imagen en base64

    with open(f'{nombre}.txt', 'w') as f: # Guarda la imagen codificada en un archivo de texto
        f.write(img_code)

# Ejemplo de uso:        
# code_jpg('images/Tablero_ajedrez.jpg','Tablero_ajedrez')