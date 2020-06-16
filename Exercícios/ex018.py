# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo = float(input("Digite o valor do ângulo para saber seu seno, cosseno e tangente: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("Para {}º\nSENO = {:.2f}\nCOSSENO = {:.2f}\nTANGENTE = {:.2f}".format(angulo, seno, cosseno, tangente))
