# ex026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase = str(input('Insira uma frase: '))
minusculas = frase.lower()


vezes = minusculas.count('a')

primeira = minusculas.index('a')

ultima = minusculas.rfind('a')


print(f'A letra "A" aparece {vezes} vezes, a primeira vez na posição {primeira} e a última na posição {ultima}!')