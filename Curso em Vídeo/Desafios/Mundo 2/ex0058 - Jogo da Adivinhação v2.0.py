'''
Melhore o jogo deo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
vencer.

'''

print('-=-' * 15)
print('       Jogo da adivinhação')
print('-=-' * 15)

'''from random import randint

rand = randint(0, 10)

''print('De 1 a 10')
adivinha = int(input('Adivinhe em qual número estou pensando: '))

cont = 1
while rand != adivinha:
    if adivinha > rand:
        adivinha = int(input('Um pouco menos... Tente novamente: '))
    else:
        adivinha = int(input('Um pouco mais... Tente novamente '))
    cont += 1
else:
    print('\nParabéns!!! Eu realmente estava pensando no número {}!'.format(adivinha))
    print('Você acertou na {}ª tentativa!'.format(cont))'''

from random import randint

rand = randint(0, 10)

print('De 1 a 10')
acertou = False
cont = 1

adivinha = int(input('Adivinhe em qual número estou pensando: '))
while not acertou:
    if adivinha < rand:
        adivinha = int(input('Um pouco mais... Tente novamente: '))
    else:
        adivinha = int(input('Um pouco menos... Tente novamente: '))
    cont += 1
    if adivinha == rand:
        acertou = True
print('Parabéns! Eu realmente estava pensando no número {}.\nVocê acertou na {}ª tentativa!'.format(adivinha, cont))
