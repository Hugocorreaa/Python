'''

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

'''

valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for x in valores:
    if x % 2 == 0:
        print(x, end=' ')




