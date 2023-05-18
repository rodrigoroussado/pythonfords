# ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

entrada = input("Escreva algo: ")
print("O tipo do dado de entrada é: {}".format(type(entrada)))

print("É alfabético? {}".format(entrada.isalpha()))
print("É numérico? {}".format(entrada.isnumeric()))
print("Só tem espaços? {}".format(entrada.isspace()))
print("Só tem caracteres ASCII? {}".format(entrada.isascii()))
print("É alfanumérico? {}".format(entrada.isalnum()))
print(f"Está todo em maiúsculas? {entrada.isupper()}")
print(f"Está todo em minúsculas? {entrada.islower()}")
print(f"Apenas inicia com uma maiúscula? {entrada.istitle()}")