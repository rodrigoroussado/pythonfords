# ex039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar 
# ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo 
# que falta ou que passou do prazo

from datetime import date

atual = date.today().year

nascimento = int(input('Insira o seu ano de nascimento: '))


idade = atual - nascimento

if (idade < 18):
    print(f'Deve alistar-se no ano de: {nascimento + 18}!')
elif (idade > 18):
    print(f'Devia ter-se alistado no ano de: {atual - (idade - 18)}!')
else:
    print('Deve alistar-se no ano corrente!')