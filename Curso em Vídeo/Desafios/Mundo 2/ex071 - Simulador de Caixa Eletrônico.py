'''

Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.

OBS. Considere que o caixa possuí cédulas de R$50, R$20, R$10 e R$1.

'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

cont50 = cont20 = cont10 = cont1 = 0

valor = int(input('Que valor você quer sacar? R$ '))

while valor != 0:
    while valor // 50 > 0:
        cont50 += 1
        valor = valor - 50
    if cont50 > 0:
        print(f'Total de {cont50} cédulas de R$50')
    while valor // 20 > 0:
        cont20 += 1
        valor = valor - 20
    if cont20 > 0:
        print(f'Total de {cont20} cédulas de R$20')
    while valor // 10 > 0:
        cont10 += 1
        valor = valor - 10
    if cont10 > 0:
        print(f'Total de {cont10} cédulas de R$10')
    while valor // 1 > 0:
        cont1 += 1
        valor = valor - 1
    if cont1 > 0:
        print(f'Total de {cont1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')