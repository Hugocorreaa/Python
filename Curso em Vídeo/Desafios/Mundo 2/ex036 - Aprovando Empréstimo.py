""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
 """

from time import sleep
print("-=-" * 15)
print("Aprovaremos o Empréstimo para Sua Casa Própria!!")
print("-=-"*15)
sleep(1)

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = float(input("Em quantos anos você pretende pagar? "))
prestação = (casa // anos) // 12
maximo = salario * 30 // 100

print("\033[1;34mAnalisando...")
sleep(1.5)

if prestação <= maximo and anos == 1:
    print("""{}Seu empréstimo foi aprovado!{}
A casa de valor R${:.2f} reais será paga em {:.0f} ano com prestações mensais de R${:.2f} reais """.format("\033[1;32m",
"\033[m", casa, anos, prestação))

elif prestação <= maximo:
    print("""{}Seu empréstimo foi aprovado!{}
A casa de valor R${:.2f} reais será paga em {:.0f} anos com prestações mensais de R${:.2f} reais """.format("\033[1;32m"
, "\033[m", casa, anos, prestação))

else:
    print("""{}Desculpa, não podemos aprovar seu empréstimo no momento!{}
Para pagar uma casa de R${:.2f} reais em {:.0f} anos a prestação mensal será de R${:.2f} reais""".format("\033[1;31m",
"\033[m", casa, anos, prestação))



