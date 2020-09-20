'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.

'''

n = int(input("Digite um número: "))

contador = soma = maior = 0
menor = n

ir = True
while ir:
    contador += 1
    soma = soma + n
    continuar = input('Deseja continuar digitando valores? [S/N] ').strip().upper()[0]
    if continuar == 'S':
        n = int(input("Digite um número: "))
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    else:
        ir = False
        media = soma / contador
        print('A média entre todos os valores é {:.2f}'.format(media))
        print('O menor valor foi {}, e o maior foi {}'.format(menor, maior))
