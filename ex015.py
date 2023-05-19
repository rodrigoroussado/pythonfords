# ex015 - Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

kms = int(input('Quantos quilómetros foram percorridos com o carro? '))
dias = int(input('Quantos dias esteve o carro alugado? '))

print(f'O preço a pagar é de {kms*0.15 + dias*60}')