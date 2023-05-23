# ex036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

casa = float((input('Insira o valor da casa: ')))
sal = float(input('Insira o valor do salário: '))
anos = int(input('Insira o número de anos de pagamento'))

prestacao = casa/anos

if (prestacao > 0.3*sal):
    print('O empréstimo está negado!')
else:
    print('O empréstimo está aprovado!')