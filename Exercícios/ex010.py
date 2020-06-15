# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27

dinheiro = float(input("Quantos reais você tem na carteira? "))
dolar = dinheiro / 3.27

print("Com a quantia de R${:.2f} reais você pode comprar US${:.2f} dólares".format(dinheiro, dolar))

