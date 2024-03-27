import cv2 
import images.dataset_pruebas as ds

cv2.imshow("Imagen-1",ds.Lechuga)

imagen_gris = cv2.cvtColor(ds.Lechuga,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen-1 Gris",imagen_gris)

cv2.waitKey(0)
