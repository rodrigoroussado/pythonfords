# ex014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit e Kelvin

celsius = float(input('Insira o valor da temperatura em graus Celsius: '))
print(f'A temperatura em Fahrenheit é {celsius*(9/5)+32} graus e em Kelvin é {celsius + 273.15}.')