# ex037 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

n = int(input('Insira um número inteiro: '))

print('''Escolha a base para a qual quer converter:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
''')

opcao = int(input('Insira a sua opção: '))

if opcao == 1:
    print(f'O número {n} em binário é: {bin(n)}')
elif opcao == 2:
    print(f'O número {n} em octal é: {oct(n)}')
elif opcao == 3:
    print(f'O número {n} em hexadecimal é: {hex(n)}')
else:
    print(f'ERRO: Opção Inválida!')