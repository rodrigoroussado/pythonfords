#ex009 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada

i = 0
n = int(input('Insira um número inteiro: '))
while i != 11:
    print(f'{n} x {i} = {n*i}')
    i = i+1