"""
Crie um programa que leia um frase qualquer e diga se ela é uma palíndromo,
desconsiderando os espaços.

ex:
Apos a sopa
A sacada da casa
A torre da derrota
O lobo ama o bolo
Anotaram a data da maratona

"""

print("-=-" * 12)
print("DETECTOR DE PALÍNDROMO")
print("-=-" * 12)


frase = str(input("Digite a frase: ")).upper().strip().split()
junto = "".join(frase)

inverso = ""
for c in range(len(junto) - 1, - 1, -1):
    inverso += junto[c]

if junto == inverso:
    print("{} ao contrário é {}\nEntão É PALÍNDROMO.".format(junto, inverso))
else:
    print("{} ao contrário é {}\nEntão NÃO É PALÍNDROMO.".format(junto, inverso))




