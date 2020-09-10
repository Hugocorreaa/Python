""" Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:

-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

"""
from datetime import date
from time import sleep
print("-=-" * 20)
print("{}SISTEMA DO SERVIÇO MILITAR!{}".format("\033[1;31m", "\033[m"))
print("-=-" * 20)
sleep(1)

nasc = int(input("Qual ano de nascimento? "))
atual = date.today().year
idade = atual - nasc
dezoito = 18 - idade
alistamento = atual + dezoito
passado = atual - (-dezoito)

if idade < 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
    print("Ainda faltam {} anos para o alistamento.".format(dezoito))
    print("Seu alistamento será no ano de {}".format(alistamento))
elif idade == 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
    print("Você deve se alistar IMEDIATAMENTE!")
else:
    print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
    print("Você já deveria ter se alistado há {} anos.".format(-dezoito))
    print("O ano do seu alistamento foi {}.".format(passado))
