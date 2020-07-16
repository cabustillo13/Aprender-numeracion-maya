import math

# El sistema de numeracion maya tiene cuatro niveles.
# Funcion para definir los niveles para escribir grandes cantidades.
def niveles(valor):
    exponente = math.log(valor,20)  #Base 20
    return (int(exponente)+1)       #Lleva +1 porque la primer capa arranca en 1

# Cada nivel puede ponerse cualquier numero del 0 al 19 
def valores(valor):
    residuo = valor%20              #Se obtiene el residuo de realizar la division respecto a 20
    return residuo                  #Si el residuo es cero significa que esa capa esta totalmente llena
    
numero = 400    
print(niveles(numero))
print(valores(numero))
