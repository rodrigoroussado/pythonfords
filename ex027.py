# ex027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Insira o seu nome completo: '))

lista = nome.split()

print(f'O primeiro nome é {lista[0]} e o último é {lista[-1]}')