# ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

oposto = float(input('Insira o comprimento do cateto oposto: '))
adjacente = float(input('Insira o comprimento do cateto adjacente: '))

print(f'O comprimento da hipotenusa é {oposto/adjacente:.3}')