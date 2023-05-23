# ex034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Insira o valor do salário: '))

if (sal <= 1250.0):
    print(f'O aumento tem valor: {0.15*sal}')
else:
    print(f'O aumento tem valor de {0.1*sal}')