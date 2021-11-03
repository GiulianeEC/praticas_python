import os
import sys

lado_1= int(input('digite o primeiro lado: '))
lado_2= int(input('digite o segundo lado: '))
lado_3= int(input('digite o terceiro lado: '))

if (lado_1 < (lado_2 + lado_3)) or (lado_2 < (lado_1 + lado_3)) or (lado_3 < lado_1 + lado_2):
    print ("é um triangulo")
    s = (lado_1 + lado_2 + lado_3) / 2
    area = (s*(s-lado_1)*(s-lado_2)*(s-lado_3))**0.5
    print('A área do triãngulo é: ', area )
else:
    print ("nao é um triangulo")

    
'''
def perimetro_triangulo(a, b, c):
    """ Calcula o perímetro de um triângulo """

    return a + b + c

def validar(a, b, c):
    if abs(b - c) < a and a < b + c:
        return True
    return False

def triangulo_eh_valido(a, b, c):
    if validar(a, b, c) and validar(b, c, a) and validar(c, a, b):
        return True
    return False

def area_triangulo(a, b, c):
    if triangulo_eh_valido(a, b, c):
        # semi-perimetro
        p = perimetro_triangulo(a, b, c)/2
        # área pela fórmula de Heron
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return area
    # triângulo impossível (inválido)
    return 0

# Num primeiro momento, gostaríamos de ter 
# um programa tão curto quanto o abaixo
# naturalmente, precisaremos dividir nossa
# solução em várias funções que resolvem
# problemas específicos e podem ser reaproveitadas
a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

area = area_triangulo(a, b, c)
print('Área do triângulo é: {}'.format(area))'''   
    