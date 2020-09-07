# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#Km para viagens de até 200Km e R$0,45 para viagens mais longas.

from time import sleep
print("-=-" * 20)
print("""Calcularei o preço de sua passagem! 
Para viagens de até 200km será cobrado R$0,50 centavos por Km.
E para viagens mais longas, será cobrado R$0,45 centavos por Km.""")
print("-=-" * 20)
sleep(1)

distancia = float(input("Qual a distância da viagem em km? "))

if distancia <= 200:
    preço1 = distancia * 0.50
    print("O preço de sua viagem de {}Km será de R${:.2f} reais.".format(distancia, preço1))
else:
    preço2 = distancia * 0.45
    print("O preço de sua viagem de {}Km será de R${:.2f} reais.".format(distancia, preço2))
