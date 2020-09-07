# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar desco
#brir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randrange
random = randrange(6)

print("-=-" * 20)
print("Vou pensar em um número de 0 a 5. Tente adivinhar!")
print("-=-" * 20)
sleep(3)

palpite = int(input("Qual número, de 0 a 5, estou pensando? "))

if palpite == random:
    print("Parabéns, você acertou! Eu estava pensando no número {}".format(random))
else:
    print("Que pena, você errou! Eu estava pensando no número {}".format(random))
