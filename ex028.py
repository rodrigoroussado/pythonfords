# ex028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random 

cpu = random.randint(0,5)


user = int(input('Tente adivinhar o número gerado: '))

if user == cpu:
    print('Ganhou!')
else:
    print('Perdeu!')
