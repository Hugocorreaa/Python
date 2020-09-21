'''

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''

print('-=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 12)

from random import randint

cont = vitoria = 0
while True:
    num = int(input('Digite um valor: '))

    # Jogada do computador:
    rand = randint(0, 10)

    # Variáveis
    soma = num + rand

    escolha = ' '
    while escolha not in 'pi':
        escolha = input('Par ou Ímpar? [P/I] ').strip().lower()[0]
        print(f'Você jogou {num} e o computador {rand}. Total de {soma}.', end=' ')
        print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
        print('-' * 55)
    if escolha == 'p':
        if soma % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'i':
        if soma % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-=-' * 12)
print(f'GAME OVER! Você venceu {vitoria} vezes.')