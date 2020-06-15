# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual o valor do salário do funcionário? R$"))
aumento = salario * 0.15
salario_aumento = salario + aumento

print("O novo salário desse funcionário, com 15% de aumento, será: R${:.2f} ".format(salario_aumento))
