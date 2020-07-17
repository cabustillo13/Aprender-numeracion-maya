import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

# El sistema de numeracion maya tiene cuatro niveles.
# Funcion para definir los niveles para escribir grandes cantidades.
def niveles(valor):
    exponente = math.log(valor,20)  #Base 20
    return (int(exponente)+1)       #Porque arranca desde el nivel 0       

# Cada nivel puede ponerse cualquier numero del 0 al 19 
def valores(valor,cociente):
    residuo = valor%cociente                #Se obtiene el residuo de realizar la division respecto a un cociente
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
        image = np.concatenate((image, cero), axis=0) #axis=0 porque se concatena horizontalmente
    
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

def resultado(valor):
    
    nivel = niveles(valor)
    
    # Iniciacion
    residuo = valores(valor,20)
    #Esta es la capa superior 
    image = numeroMaya(residuo)
    
    for x in range(nivel-1):
        
        #Actualizacion de variable
        valor = valor - residuo
        residuo = valores(valor,pow(20,x+2))
        
        aux = numeroMaya(residuo)
        aux = np.concatenate((image, aux), axis=0)
            
    return image
  
# Probar codigo
#imagen = numeroMaya(20)
#plt.imshow(imagen)
#plt.axis("off")
#plt.show()

#Acorde a la historia este sistema numeracion maya tiene cuatro niveles, que se utilizaban para escribir grandes cantidades.
#Matematicamente f(x) = x1 + 20*x2 + 400*x3 + 8000*x4
#def getCoeficientes(valor):
#    x1,x2,x3,x4=0,0,0,0
    
#    x1 = valores(valor,20)
#    valor = valor - x1
    
#    x4 = valor/8000
#    valor = valor -8000*x4
    
#    x3 = valor/400
#    valor = valor - 400*x3
    
#    x2 = valor/20
#    valor = valor - 20*x2
    
#    return x4,x3,x2,x1

#Probar codigo
#x4,x3,x2,x1 = getCoeficientes(481)
#print(x4,x3,x2,x1)

def getCoeficientes(valor):
    
    coeficientes = list()
    for i in range(4):
        
        x = (valor)/(20**(3-i))
        valor = valor - (20**(3-i))*x
        coeficientes.append(x)
    
    return coeficientes

#Probar codigo
#coeficientes = getCoeficientes(481)
#print(coeficientes)
