# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:16:05 2021

@author: angelica
"""
"""
Prueba: sección suma impares, Parte 1
"""
"""
Descripción del problema:
    En este problema realizaremos sumatorias, con la condición que el número
    a sumar será impar.
    
    Parte 1:
        Crea programa donde se sumen todos los valores impares desde 0 hasta n,
        donde n es ingresado por el usuario.
        Si n=6. la salida del programa deberá ser: 9
        que corresponde a sumar 1+3+5
"""    
def ingreso_dato():
    #mensaje para que el usuario sepa cuando ingresar el numero 
    print("ingrese un numero desde el teclado")
    #Variable que almacena el dato ingresado por el usuario
    dato=input()
    # se retorna el dato del usuario fuera de la funcion para trabajar con el.
    return dato

def sum_impares(dato):
    suma_im=0
    for i in range (0,dato):
        #La variable i recorre el numero del usuario con un incremento de 1
        n=i%2 # Se saca la funcion resto de cada valor que toma la variable i
        #si el resto es 1, se asume numero impar, por lo que se ingresa para una posterior suma
        if n==1:
            suma_im=suma_im+i#Variable que almacena la suma de los numero impares 
    print("===============Resultado========================")
    print(suma_im)# impresion del dato por pantalla  
    


# Se transforma el tipo de dato ingresado por el usuario, que es de tipo str
# al formato INT con el que se puede tratar como numero "natural", esto permite
# realizar las operaciones tradicionales con dicho dato.
x=int(ingreso_dato())
sum_impares(x)    
    