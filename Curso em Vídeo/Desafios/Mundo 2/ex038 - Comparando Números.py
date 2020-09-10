""" Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:

-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais

"""

from time import sleep
print("-=-" * 20)
print("Digite dois números inteiros para saber qual é o maior.")
print("-=-" * 20)
sleep(1)

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print("{} é maior que {}. Logo, o PRIMEIRO valor é maior.".format(num1, num2))
elif num2 > num1:
    print("{} é maior que {}. Logo, o SEGUNDO valor é maior.".format(num2, num1))
else:
    print("Não existe valor maior, os dois são IGUAIS.")
