""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

-Á vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2x no cartão: Preço Normal
-3x ou mais no cartão: 20% de Juros
"""

valor = float(input("Digite o valor do produto: R$"))
print("""Qual a forma de pagamento?
[1] Dinheiro ou Cheque.
[2] Á vista no cartão.
[3] Em até 2x no cartão.
[4] 3x ou mais no cartão.""")

pag = int(input("Sua opção: "))
if pag == 1:
    descont = valor - (valor * 10 // 100)
    print("""Com pagamento em dinheiro ou cheque você tem 10% de desconto.
Valor com desconto: R${:.2f} reais""".format(descont))
elif pag == 2:
    descont = valor - (valor * 5 // 100)
    print("""Com pagamento à vista no cartão você tem 5% de desconto.
Valor com desconto: R${:.2f} reais""".format(descont))
elif pag == 3:
    par = valor / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.".format(par))
    print("Valor final: R${:.2f} reais".format(valor))
elif pag == 4:
    parcelas = int(input("Quantas parcelas? "))
    par = valor / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM 20% DE JUROS.".format(parcelas, par))
    juros = (valor * 20 / 100) + valor
    print("Valor com juros: R${:.2f} reais".format(juros))
else:
    print("\033[1;31mOperação Inválida!\033[m")
