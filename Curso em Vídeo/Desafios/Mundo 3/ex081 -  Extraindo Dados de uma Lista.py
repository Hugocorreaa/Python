'''

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

'''

lista = []
cont = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
    cont += 1

print('-=' * 30)
print(f'Você digitou {cont + 1} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
