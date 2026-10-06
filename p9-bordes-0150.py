#Zavala Medina Alexia Paola
# NC= 0150
import cv2
import numpy as np

# Cargar la imagen del mapache
imagen = cv2.imread("Mapache.jpg")

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro Gaussiano para reducir el ruido
imagen_suavizada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

# Aplicar el algoritmo Canny para la detección de bordes
bordes_canny = cv2.Canny(imagen_suavizada, 100, 200)

# Mostrar las imágenes en ventanas
cv2.imshow("Imagen Original - Mapache", imagen)
cv2.imshow("Escala de Grises", imagen_gris)
cv2.imshow("Detección de Bordes - Canny", bordes_canny)

# Guardar el resultado en la misma carpeta
cv2.imwrite("Mapache_bordes.jpg", bordes_canny)
print("La imagen con los bordes detectados se guardó como 'Mapache_bordes.jpg'")

# Esperar a que se presione cualquier tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Zavala Medina NC = 0150")