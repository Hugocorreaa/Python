'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1 = 120

'''

print("-=-" * 15)
print("Cálculo de Fatorial")
print("-=-" * 15)

n = int(input('Digite o número para saber seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end="")
    print(" x " if c > 1 else ' = ', end="")
    f = f * c
    c -= 1
print(f)
