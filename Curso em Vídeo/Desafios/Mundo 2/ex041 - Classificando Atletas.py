""" A Confederação Nacional de Natação precisa de um program que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 25 anos: Sênior
-Acima: Master
"""

from datetime import date
nasc = int(input("Qual ano de nascimento do atleta? "))
idade = date.today().year - nasc

if idade <= 9:
    print("O atleta tem {} anos e se classica na categoria: {}Mirim{}".format(idade, "\033[1;34m", "\033[m"))
elif idade <= 14:
    print("O atleta tem {} anos e se classifica na categoria: {}Infantil{}".format(idade, "\033[1;34m", "\033[m"))
elif idade <= 19:
    print("O atleta tem {} anos e se classifica na categoria: {}Junior{}".format(idade, "\033[1;34m", "\033[m"))
elif idade <= 25:
    print("O atleta tem {} anos e se classifica na categoria: {}Sênior{}".format(idade, "\033[1;34m", "\033[m"))
else:
    print("A atleta tem {} anos e se classifica na categoria: {}Master{}".format(idade, "\033[1;34m", "\033[1;34m"))
