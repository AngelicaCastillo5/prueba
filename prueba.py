# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ingreso_dato():
    #mensaje para que el usuario sepa cuando ingresar el numero 
    print("ingrese un numero por favor")
    #Variable que almacena el dato ingresado por el usuario
    dato=input()
    # se retorna los datos del usuario fuera de la funcion para trabajar con el.
    return dato

def serie_fibonacci(dato):# se añaden los datos de usuario
    #inicializacion de variables    
    FB=0
    FBF=0
    FBS=1
    print("===============Resultado========================")
    #Secuencia de recorrido
    for i in range (0,dato+2):# se utilizan los datos del usuario como limites
        #La variable i recorre el numero del usuario con un incremento de 1
        if i==0:
            print(FBF)
        if i==1:
            print(FBS)
        if i>2:
            FB=FBF+FBS
            FBF=FBS
            FBS=FB
            print(FB)
 
    

x=ingreso_dato() # se almacenan los datos ingresados por el usuario en las variables x e y 
# Se transforma el tipo de dato ingresado por el usuario, que es de tipo str
# al formato INT con el que se puede tratar como numero "natural", esto permite
# realizar las operaciones tradicionales con dicho dato.
x=int(x)

#Se llama a la funcion, con los datos ingresados por el usuario 
serie_fibonacci(x)