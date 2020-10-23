'''

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''

lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar: [S/N] '))
    if continuar in 'Nn':
        break

for valor in lista:
    if valor % 2 == 0:
        par.append(int(valor))
    else:
        impar.append(int(valor))

print('-=-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
