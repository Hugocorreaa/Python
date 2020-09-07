# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
from time import sleep
print("-=-" * 15)
print("Lhe direi se o ano é Bissexto ou não.")
print("-=-" * 15)
sleep(1)

print("Se deseja saber se o ano atual é bissexto, digite 0")
ano = int(input("Digite o ano que você deseja saber: "))

sleep(1.5)
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print("Sim! O ano de {} é bissexto!".format(ano))
else:
    print("Não! O ano de {} não é bissexto!".format(ano))

