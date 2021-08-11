# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:59:55 2021

@author: angelica
"""

"""
Prueba: sección suma impares, Parte 2
"""
"""
Descripción del problema:
    En este problema realizaremos sumatorias, con la condición que el número
    a sumar será impar.
    
    Parte 2:
        Crea programa, donde el usuario ingresa dos valores,
        el limite inferior (min) y superior (max) del intervalo
        para realizar la suma de los impares.
        Si min=6 y max=30, la salida del programa deberá ser: 216
        que corresponde a sumar 7+9+11+13+15+17+19+21+23+25+27+29
"""    
def ingreso_dato():
    #mensaje para que el usuario sepa cuando ingresar el numero 
    print("instrucciones: El usuario debe ingresar dos numeros, uno que representa el limite inferior y uno que sea el limite superior")
    print("ingrese un numero que corresponda al limite inferior por favor")
    #Variable que almacena el limite inferior ingresado por el usuario
    dato=input()
    print("ingrese un numero que corresponda al limite Superior por favor")
    #Variable que almacena el limite superior ingresado por el usuario
    dato1=input()
    # se retorna los datos del usuario fuera de la funcion para trabajar con el.
    return dato, dato1

def sum_impares(dato,dato1):# se añaden los datos de usuario
    suma_im=0
    for i in range (dato,dato1):# se utilizan los datos del usuario como limites
        #La variable i recorre el numero del usuario con un incremento de 1
        n=i%2 # Se saca la funcion resto de caa valor que toma la variable i
        #si el resto es cero, se imprime el numero correspondiente a los primeros pares del dato ingresado por el usuario.
        
        if n==1:
            suma_im=suma_im+i
    print("===============Resultado========================")
    print(suma_im)# impresion del dato por pantalla  
    

x,y=ingreso_dato() # se almacenan los datos ingresados por el usuario en las variables x e y 
# Se transforma el tipo de dato ingresado por el usuario, que es de tipo str
# al formato INT con el que se puede tratar como numero "natural", esto permite
# realizar las operaciones tradicionales con dicho dato.
x=int(x)
y=int(y)
#Se llama a la funcion que suma los impares, con los datos ingresados por el usuario 
sum_impares(x,y)