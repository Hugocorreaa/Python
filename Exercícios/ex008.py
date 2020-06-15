# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite o valor em metros a ser convertido: "))
kilo = metros / 1000
hecto = metros / 100
deca = metros / 10
deci = metros * 10
cent = metros * 100
mili = metros * 1000

print("{} metros equivale à:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm ".format(metros, kilo, hecto, deca, deci,
cent, mili))
