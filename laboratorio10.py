# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:29:41 2020

@author: Juan Rojas
"""


def a_power_b(a,b,resultado):
    if a == 0:
        print("no esta definida")
    else:
            
     for i in range(b):
        resultado = resultado*a
    return resultado

a = int(input("ingrese el numero base"))
b = int(input("ingrese el numero de exponente"))
    
resultado = 1

print("la potencia es:" + str (a_power_b(a,b,resultado)))


