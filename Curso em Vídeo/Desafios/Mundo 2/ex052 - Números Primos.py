"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""

numero = int(input("Digite um número: "))

contador = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print("\033[34m", end=" ")
        contador += 1
    else:
        print("\033[31m", end=" ")
    print("{} ".format(c), end=" ")
if contador == 2:
    print("""\n\033[mO número {} foi divisível {} vezes.
E por isso ele É PRIMO!""".format(numero, contador))
else:
    print("""\n\033[mO número {} foi divisível {} vezes.
E por isso ele NÃO É PRIMO!""".format(numero, contador))
