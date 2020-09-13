"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já não maiores.

maior idade = 21 anos

"""

from datetime import date
atual = date.today().year

maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input("Que ano a {}ª pessoa nasceu? ".format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("\n{} pessoas já atingiram a maioridade.\nE {} pessoas não atingiram a maioridade ainda.".format(maior, menor))
