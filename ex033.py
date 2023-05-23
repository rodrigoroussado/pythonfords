# ex033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor


n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

lista = [n1,n2,n3]

print(f'O maior número é o: {max(lista)} e o menor é o: {min(lista)}')