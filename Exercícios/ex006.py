# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = float(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print("O dobro de {:.0f} é {:.0f}.\nSeu triplo é {:.0f}.\nSua raiz quadrada é {:.2f}.".format(numero, dobro, triplo, raiz))
