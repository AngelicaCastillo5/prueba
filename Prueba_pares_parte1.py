# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:51:14 2021

@author: angelica
"""

"""
Prueba: sección solo pares, Parte 1
"""
"""
Descripción del problema:
    El programa debe recibir un parametro "n" ingresado por el usuario
    y mostrar los primeros "n" pares.
    Si n=4, la salida del programa deberá ser: 
        0
        2
        4
        6
        
"""    
#funcion "ingreso_dato", esta funcion pide al usuario que ingrese un numero 
# el teclado del computador
def ingreso_dato():
    #mensaje para que el usuario sepa cuando ingresar el numero 
    print("ingrese un numero desde el teclado")
    #Variable que almacena el dato ingresado por el usuario
    dato=input()
    # se retorna el dato del usuario fuera de la funcion para trabajar con el.
    return dato


#Funcion en donde se obtienen los numeros pares del dato ingresado por el usuario
def pares_con_cero(dato): 
    par=0
    total=0
    n=0
    while n<dato:
        if n==0:
            par=0
            total=0
        if n>0:
            total=par+2
            par=total
        print(total)
        n=n+1

# Se transforma el tipo de dato ingresado por el usuario, que es de tipo str
# al formato INT con el que se puede tratar como numero "natural", esto permite
# realizar las operaciones tradicionales con dicho dato.
x=int(ingreso_dato())
print("===============Resultado========================")
pares_con_cero(x)

