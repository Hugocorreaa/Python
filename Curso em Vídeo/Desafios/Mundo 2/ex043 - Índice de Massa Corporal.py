""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade Mórbida
"""

from time import sleep
print("-=-" * 20)
print("CALCULADORA DE IMC")
print("-=-" * 20)
sleep(1)

peso = float(input("Qual seu peso atual? (Kg) "))
altura = float(input("Qual sua altura? (m) "))
imc = peso / (altura ** 2)

print("O seu IMC, baseado na seu peso de {}Kg e sua altura de {}m é de: {}{:.1f}Kg/m²{}".format(peso, altura, "\033[1;34m", imc, "\033[m"))

if imc <= 18.5:
    print("Você está {}ABAIXO{} do peso ideal.".format("\033[1;31m", "\033[m"))
elif 18.6 < imc <= 25:
    print("Você está no {}PESO IDEAL{}.".format("\033[1;34m", "\033[m"))
elif 25.1 <= imc <= 30:
    print("Você está com {}SOBREPESO{}.".format("\033[1;33m", "\033[m"))
elif 30.1 <= imc <= 40:
    print("Você está com {}OBESIDADE{}.".format("\033[1;31m", "\033[m"))
else:
    print("Você está com {}OBESIDADE MÓRBIDA{}.".format("\033[1;31m", "\033[m"))
