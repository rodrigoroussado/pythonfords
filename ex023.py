# ex023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

n = int(input('Insira um número de 0 a 9999: '))

unidade = n // 1 % 10 # "Retira" os dígitos do número da direita para a esquerda
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print(f'''
Milhares: {milhar}
Centenas: {centena}
Dezenas: {dezena}
Unidades: {unidade}
''')