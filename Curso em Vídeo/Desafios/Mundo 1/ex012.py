# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preçoProduto = float(input("Qual o valor do produto? R$"))
desconto = preçoProduto * 0.05
preçoDesconto = preçoProduto - desconto

print("O preço do produto com 5% de desconto será R${:.2f} reais".format(preçoDesconto))
