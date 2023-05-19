# ex018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import *

ang = float(input('Insira o valor do ângulo (em graus): '))
rad = radians(ang)

print(f'sen({ang}) = {sin(rad):.2} \n cos({ang}) = {cos(rad):.2} \n tan({ang}) = {tan(rad):.2}')