# ex024 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Insira o nome da cidade onde nasceu: '))
lista = cidade.split()

if lista[0] == 'Santo':
    print('O nome começa por "Santo". ')
else:
    print('O nome não começa por "Santo."')