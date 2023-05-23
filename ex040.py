# ex040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo 
# com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Insira a nota do primeiro teste: '))
nota2 = float(input('Insira a nota do segundo teste: '))

media = (nota1 + nota2)/2

if (media > 7.0):
    print('APROVADO')
elif (media < 5.0):
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')