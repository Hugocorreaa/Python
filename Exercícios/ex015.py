# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorridos = float(input("Quantos Km foram percorridos? "))
diasAlugados = int(input("Por quantos dias o carro foi alugado? "))
preço = (diasAlugados * 60) + (kmPercorridos * 0.15)

print("O preço a pagar será: R${}".format(preço))
