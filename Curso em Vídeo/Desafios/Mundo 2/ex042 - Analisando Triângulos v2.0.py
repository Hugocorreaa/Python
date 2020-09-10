""" Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo erá formado:

-Equilátero: Todos os lados iguais
-Isósceles: Dois lados iguais
-Escaleno: Todos os lados diferentes
"""

from time import sleep
print("-=-" * 25)
print("Me diga 3 medidas de reta que lhe direi se é possível formar um triangulo.")
print("-=-" * 25)
sleep(1)

a = float(input("Digite a primeira medida: "))
b = float(input("Digite a segunda medida : "))
c = float(input("Digite a terceira medida: "))

if a + b > c and a + c > b and b + c > a:
    print("Sim! É possível formar um triangulo com essas medidas.")
    if a == b == c:
        print("Será formado um triângulo {}EQUILÁTERO{}, pois todos os lados são iguais.".format("\033[1;34m", "\033[m"))
    elif (a == b != c) or (b == c != a) or (c == a != b):
        print("Será formado um triângulo {}ISÓSCELES{}, pois somente dois lado são iguais.".format("\033[1;34m", "\033[m"))
    elif a != b != c:
        print("Será formado um triângulo {}ESCALENO{}, pois todos os lados são diferentes.".format("\033[1;34m", "\033[m"))
else:
    print("Não! É impossível formar um triangulo com essas medidas.")
