"""

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se for ímpar, desconsidere-o.

"""

n = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite o {}º valor: ".format(c)))
    if n % 2 == 0:
        n += n
        cont += 1
print("Você informou {} números pares e a soma deles é {}.".format(cont, n))
