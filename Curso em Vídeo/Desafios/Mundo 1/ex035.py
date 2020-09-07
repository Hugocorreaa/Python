# Desenvolva um programa que leia o cumprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

from time import sleep
print("-=-" * 25)
print("Me diga 3 medidas de reta que lhe direi se é possível formar um triangulo")
print("-=-" * 25)
sleep(1.5)

a = float(input("Digite a primeira medida: "))
b = float(input("Digite a segunda medida : "))
c = float(input("Digite a terceira medida: "))

if a + b > c and a + c > b and b + c > a:
    print("Sim! É possível formar um triangulo com essas medidas.")
else:
    print("Não! É impossível formar um triangulo com essas medidas.")
