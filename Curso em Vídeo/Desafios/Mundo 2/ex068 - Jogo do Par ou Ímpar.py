'''

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''

print('-=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 12)

from random import randint


cont = 0
while True:
    num = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').strip().lower()[0]
    print('-' * 55)

    rand = randint(1, 10)
    soma = num + rand
    cont += 1

    if soma % 2 == 0 and escolha == "p":
        print(f'Você jogou {num} e o computador {rand}. Total de {soma}. DEU PAR')
        print('-' * 55)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(('-=-' * 12))
    elif soma % 2 == 0 and escolha == "i":
        print(f'Você jogou {num} e o computador {rand}. Total de {soma}. DEU PAR')
        print('-' * 55)
        print('Você PERDEU!!')
        print('-=-' * 12)
        print(f'GAME OVER! Você venceu {cont} vezes')
        break
    elif soma % 2 != 0 and escolha == "i":
        print(f'Você jogou {num} e o computador {rand}. Total de {soma}. DEU ÍMPAR')
        print('-' * 55)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(('-=-' * 12))
    elif soma % 2 != 0 and escolha == "p":
        print(f'Você jogou {num} e o computador {rand}. Total de {soma}. DEU ÍMPAR')
        print('-' * 55)
        print('Você PERDEU!!')
        print('-=-' * 12)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break