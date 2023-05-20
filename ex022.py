# ex022 - 
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Insira o seu nome completo: '))

# Separar o nome em várias palavras
listaNomes = nome.split()
primeiroNome = listaNomes[0]

# Retirar os espaços ao nome
semEspaco = nome.replace(" ", "")

print(f'Todo em maiúsculas: {nome.upper()} \nTodo em minúsculas: {nome.lower()} \nSem espaços: {semEspaco}')
print(f'Tem {len(semEspaco)} letras \nO primeiro nome tem: {len(primeiroNome)} letras')