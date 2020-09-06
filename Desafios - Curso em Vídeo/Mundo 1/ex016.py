""" Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteiro.
Ex: Digite um número: 6.127
O numero 6.127 tem a porção inteira 6 """

from math import trunc
numeroReal = float(input("Digite um número para saber sua porção inteira: "))
print("A porção inteira de {} é {}".format(numeroReal, trunc(numeroReal)))  # Também posso escrever "int(numeroReal)"

