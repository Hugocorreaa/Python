'''

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar: [S/N] '))
    if continuar in 'Nn':
        break
print('A 'lista)
print(lista)