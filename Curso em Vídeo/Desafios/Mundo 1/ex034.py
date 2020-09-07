# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep
print("-=-" * 15)
print("Calcularei o valor do aumento do seu salário")
print("-=-" * 15)
sleep(1.5)

salario = float(input("Digite o valor do seu salário: R$"))

if salario > 1250:
    aumento = (salario * 10 // 100)
    novo = salario + aumento
    print("Seu aumento será de R${:.2f} e seu novo salário será R${:.2f}".format(aumento, novo))
else:
    aumento = (salario * 15 // 100)
    novo = salario + aumento
    print("Seu aumento será de R${:.2f} e seu novo salário será de R${:.2f}".format(aumento, novo))
