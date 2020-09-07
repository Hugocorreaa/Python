# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número : "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 < numero2 < numero3:
    print("{} é o maior número.".format(numero3))
    print("{} é o menor número.".format(numero1))
if numero1 > numero2 > numero3:
    print("{} é o maior número.".format(numero1))
    print("{} é o menor número.".format(numero3))
if numero1 > numero2 < numero3:
    print("{} é o maior número.".format(numero1))
    print("{} é o menor número.".format(numero2))
if numero2 < numero1 < numero3:
    print("{} é o maior número.".format(numero3))
    print("{} é o menor número.".format(numero2))
if numero2 > numero1 > numero3:
    print("{} é o maior número.".format(numero2))
    print("{} é o menor número.".format(numero3))
if numero3 < numero1 < numero2:
    print("{} é o maior número".format(numero2))
    print("{} é o menor número".format(numero3))
if numero2 > numero1 < numero3:
    print("{} é o maior número".format(numero2))
    print("{} é o menor número".format(numero1))


"""Maneira mais simples de resolver:

menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero 2:
    menor = numero3
    
#verificando maior

maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero 2:
    maior = numero3
    
print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
"""