## ex011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
## quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Insira, em metros, a largura da parede: '))
altura = float(input('Insira, em metros, a altura da parede: '))

print(f'A parede tem uma área de {largura*altura} metros e são necessários {(largura*altura)/2} litros para a pintar.')