import cv2 
import numpy as np
import images.dataset_pruebas as ds

# ----- Función para filtrar -----
def filtrar(n,m,filtro,imagen):
    matriz_aux = np.ones((n,m))
    matriz_aux*=255
    for i in range(1,n-1):
        for j in range(1,m-1):
            aux = imagen[i,j]*filtro[1][1] + imagen[i-1,j]*filtro[0][1] + imagen[i+1,j]*filtro[2][1] + imagen[i,j-1]*filtro[1][0] + imagen[i,j+1]*filtro[1][2] + imagen[i-1,j-1]*filtro[0][0] + imagen[i-1,j+1]*filtro[0][2] + imagen[i+1,j-1]*filtro[2][0] + imagen[i+1,j+1]*filtro[2][2] 

            if aux > 255:
                aux = 255
            if aux < 0:
                aux = 0

            matriz_aux[i,j] = aux
    matriz_aux=matriz_aux.astype(np.uint8)
    return matriz_aux
# ----- Función para filtrar -----

# ----- Filtros ------------------
f_1 = [[0,-1,0], # filtro lapaciano 
       [-1,4,-1],
       [0,-1,0]]

f_2 = [[1,1,1],
       [1,8,1],
       [1,1,1]]
# ----- Filtros ------------------

imagen = ds.Tablero_ajedrez
matriz = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
cv2.imshow("Tablero de ajedrez - Grises",matriz)

n,m = matriz.shape

matriz_filtrada = filtrar(n,m,f_2,matriz)
cv2.imshow("Tablero de ajedrez - Filtrado",matriz_filtrada)
cv2.waitKey(0)