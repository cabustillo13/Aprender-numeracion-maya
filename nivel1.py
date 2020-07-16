import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

# El sistema de numeracion maya tiene cuatro niveles.
# Funcion para definir los niveles para escribir grandes cantidades.
def niveles(valor):
    exponente = math.log(valor,20)  #Base 20
    return (int(exponente)+1)       #Lleva +1 porque la primer capa arranca en 1

# Cada nivel puede ponerse cualquier numero del 0 al 19 
def valores(valor,cociente):
    residuo = valor%cociente                #Se obtiene el residuo de realizar la division respecto a 20
    return residuo                          #Si el residuo es cero significa que esa capa esta totalmente llena

    
# Crear una imagen con su respectiva representacion maya para cada numero
# Cada numero debe ser menor de 20, que es la representacion maxima que se puede realizar por cada nivel
def numeroMaya(numero): 
    
    # Comenzamos la imagen con un pequeno margen, sobre cual empezaremos a concatenar
    image = cv2.imread('./Imagenes1/margen.png')
    
    cero = cv2.imread("./Imagenes1/A0.png")
    uno = cv2.imread("./Imagenes1/A1.png")
    dos = cv2.imread("./Imagenes1/A2.png")
    tres = cv2.imread("./Imagenes1/A3.png")
    cuatro = cv2.imread("./Imagenes1/A4.png")
    cinco = cv2.imread("./Imagenes1/A5.png")
    
    # Para el cero maya 
    residuo = valores(numero,5)
    
    if (numero == 0):
        image = np.concatenate((image, cero), axis=0)
    
    # Para el punto maya
    else:
        if (residuo == 1):
            image = np.concatenate((image, uno), axis=0)
        elif (residuo == 2):
            image = np.concatenate((image, dos), axis=0)
        elif (residuo == 3):
            image = np.concatenate((image, tres), axis=0)
        elif (residuo == 4):
            image = np.concatenate((image, cuatro), axis=0)
            
    # Para la barra maya
    for x in range(int(numero/5)):
        if (numero >= 5) :
            image = np.concatenate((image, cinco), axis=0)
        else:
            image = np.concatenate((image, cinco), axis=0)

    return image

# Probar codigo
#imagen = numeroMaya(20)
#plt.imshow(imagen)
#plt.axis("off")
#plt.show()
