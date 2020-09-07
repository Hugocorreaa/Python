# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Em qual velocidade o carro está? "))

if velocidade <= 80:
    print("Você não ultrapassou o limite de 80Km/h e não será multado.")
else:
    multa = (velocidade - 80) * 7
    print("Você ultrapassou o limite de 80Km/h. Você será MULTADO em R${:.2f} reais!".format(multa))
