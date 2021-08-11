# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:06:29 2021

@author: angelica
"""

"""
Prueba: sección solo pares, Parte 2
"""
"""
Descripción del problema:
   Ahora deberá crear el program, donde no se considere el cero. 
    Si n=4, la salida del programa deberá ser: 
        2
        4
        6
        8
        
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

         
def pares(dato): 
    par=0
    total=0
    n=0
    while n<dato:
        
        total=par+2
        par=total
        print(total)
        n=n+1
    
    
    
# Se transforma el tipo de dato ingresado por el usuario, que es de tipo str
# al formato INT con el que se puede tratar como numero "natural", esto permite
# realizar las operaciones tradicionales con dicho dato.
x=int(ingreso_dato())
print("===============Resultado========================")
pares(x)
