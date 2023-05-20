# ex029 - Escreva um programa que leia avelocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7,00€ por cada Km acima do limite

velocidade = int(input('Insira a velocidade do carro (em Km/h): '))

if (velocidade > 80):
    print(f'A multa vai ter valor de {7*(velocidade - 80)}€!')
else:
    print('Não tem multa!')