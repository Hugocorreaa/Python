'''

Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.

'''

print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

tot = mil = menor = cont = 0
barato = ' '

while True:
    nome = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))

    cont += 1
    tot += p
    if p > 1000:
        mil += 1
    if cont == 1 or p < menor:
        menor = p
        barato = nome

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

    if continuar == 'n':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato.capitalize()} que custa R${menor:.2f}')