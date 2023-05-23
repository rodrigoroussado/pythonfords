# ex035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

l1 = float(input('Insira o comprimento do primeiro lado: '))
l2 = float(input('Insira o comprimento do segundo lado: '))
l3 = float(input('Insira o comprimento do último lado: '))

lista = [l1,l2,l3]
maior = max(lista)
del(lista[max(lista)])

if (lista[0] + lista[1] < max(lista)):
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')