'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma Sequência de Fibonacci.

ex. 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

'''

print('-=-' * 15)
print('Sequência de Fibonacci')
print('-=-' * 15)

n = int(input('Quantos termos você quer mostrar? '))

contador = 2
f1 = 0
f2 = 1
print('{} -> {}'.format(f1, f2), end=" ")

while contador < n:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    contador += 1
    print('-> {}'.format(fn), end=" ")
print('-> FIM')

