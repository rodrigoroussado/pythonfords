# ex031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço do bilhete, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

distancia = float(input('Insira a distância da viagem (em Km): '))

if (distancia <= 200):
    print(f'O preço do bilhete vai ser de {0.5*distancia}$')
else:
    print(f'O preço do bilhete vai ser de {0.45*distancia}$')