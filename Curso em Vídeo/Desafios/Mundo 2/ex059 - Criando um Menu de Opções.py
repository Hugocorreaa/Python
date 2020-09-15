'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverás realizar a operação solicitada em cada caso.

'''

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))


opção = 0
while opção != 5:
    print('''\n---MENU DE ESCOLHAS---
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMERO
    [5] SAIR DO PROGRAMA
    ''')
    opção = int(input('>>>>>> Escolha a operação: '))
    if opção == 1:
        resultado = valor1 + valor2
        print("A soma entre {:.0f} + {:.0f} resulta em {:.0f}".format(valor1, valor2, resultado))
    elif opção == 2:
        resultado = valor1 * valor2
        print('A multiplicação entre {:.0f} x {:.0f} resulta em {:.0f}'.format(valor1, valor2, resultado))
    elif opção == 3:
        if valor1 > valor2:
            print('{:.0f} é maior que {:.0f}'.format(valor1,valor2))
        else:
            print('{:.0f} é maior que {:.0f}'.format(valor2, valor1))
    elif opção == 4:
        valor1 = float(input('\nDigite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    else:
        opção = int(input("Opção inválida. Digite novamente: "))
    print('=-=' * 15)
print('Programa finalizado.')
