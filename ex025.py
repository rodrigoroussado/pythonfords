# ex025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Insira o seu nome completo: '))
lista = nome.split()
bool = 'Silva' in lista

print(f'O nome tem "Silva": {bool}')