import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

# El sistema de numeracion maya tiene cuatro niveles.
# Funcion para definir los niveles para escribir grandes cantidades.
def getNiveles(valor):
    
    if valor != 0:
        exponente = math.log(valor,20)  #Base 20
        return (int(exponente)+1)       #Porque arranca desde el nivel 0
    else:
        return 1

# Cada nivel puede ponerse cualquier numero del 0 al 19 
def valores(valor,cociente):
    residuo = valor%cociente                #Se obtiene el residuo de realizar la division respecto a un cociente
    return residuo                          #Si el residuo es cero significa que esa capa esta totalmente llena

    
# Crear una imagen con su respectiva representacion maya para cada numero
# Cada numero debe ser menor de 20, que es la representacion maxima que se puede realizar por cada nivel
def numeroMaya(numero): 
    
    # Comenzamos la imagen con un pequeno margen, sobre cual empezaremos a concatenar
    image = cv2.imread('./Imagenes/margen.png')
    
    cero = cv2.imread("./Imagenes/A0.png")
    uno = cv2.imread("./Imagenes/A1.png")
    dos = cv2.imread("./Imagenes/A2.png")
    tres = cv2.imread("./Imagenes/A3.png")
    cuatro = cv2.imread("./Imagenes/A4.png")
    cinco = cv2.imread("./Imagenes/A5.png")
    
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
    
    nivel = getNiveles(valor)
    
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
  
#Acorde a la historia este sistema numeracion maya tiene cuatro niveles, que se utilizaban para escribir grandes cantidades.
#Matematicamente f(x) = x1 + 20*x2 + 400*x3 + 8000*x4
def getCoeficientes(valor):
    
    coeficientes = list()
    for i in range(4):
        
        x = int((valor)/(20**(3-i)))
        valor = valor - (20**(3-i))*x
        coeficientes.append(x)
    
    #Los coeficientes se devuelven de esta forma [x4,x3,x2,x1]
    return coeficientes

def unirNiveles(coeficientes,nivel,valor):
    
    for i in range(4):
        # Todo numero entero tiene al menos un nivel
        if (i==0):
            image = numeroMaya(coeficientes[3-i])
        else:
            aux = numeroMaya(coeficientes[3-i])
            if (i < nivel): #Se concatenara solo los valores que no superen el nivel maximo
                image = np.concatenate((aux , image), axis=0)
    
    # Terminamos la imagen con un pequeno margen
    margen = cv2.imread('./Imagenes/margen.png')
    encabezado = escribirValor(valor)
    image = np.concatenate((encabezado,image,margen),axis=0)
    
    return image

# Permite escibir el valor dentro de la imagen
def escribirValor(valor):
    
    image = cv2.imread('./Imagenes/margen.png')
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    texto = str(valor)
    
    #Obtener tamano del texto
    textsize = cv2.getTextSize(texto, fuente, 9, 5)[0]
    
    #Obtener coordenadas
    X = int((image.shape[1] - textsize[0]) / 2)
    Y = int((image.shape[0] - textsize[1]) / 2)
    
    # Escribir texto en la imagen
    cv2.putText(image, texto, (X,Y+215), fuente, 9, (0, 0, 0), 5) # Se sumo 215 px a Y para colocar por debajo del centro
    #cv2.putText(imagen,texto, (coordenadas),tamano fuente,(color RGB),grosor)
    
    return image

if __name__ == "__main__":
    
    #Numero a analizar
    numero = int(input("Ingresar numero arabigo: "))
    
    #Recordad que el maximo valor que se puede representar, respetando los 4 niveles es 159999
    if (numero < 160000):
        nivel = getNiveles(numero)
        coeficientes = getCoeficientes(numero)
        imagen = unirNiveles(coeficientes,nivel,numero)
    
        # Ver resultados
        plt.imshow(imagen)
        plt.axis("off")
        plt.show()
    
        # Guardar imagen
        # Como los nombres de archivos no pueden arrancar con un numero, anteponemos la letra A y luego el numero
        path = "./Resultados/A" + str(numero) + ".png"
        cv2.imwrite(path,imagen)
    
    else:
        print("\nTu numero excede el rango permitido")
        print("Segun la historia, solo se puede representar hasta el valor 159999")
    
