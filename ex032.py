# ex032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Insira o ano: '))

if (ano % 4 == 0):
    print('O ano é bissexto!')
else:
    print('O ano é comum!')