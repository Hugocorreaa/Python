# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep
print("-=-" * 15)
print("Vou descobrir se o número é ímpar ou par!")
print("-=-" * 15)
sleep(1)

numero = int(input("Qual número você quer que eu descubra? "))

if numero % 2 == 0:
    print("O número {} é par!".format(numero))
else:
    print("O número {} é ímpar!".format(numero))
