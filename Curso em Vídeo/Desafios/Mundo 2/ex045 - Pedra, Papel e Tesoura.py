""" Crie um programa que faça o computador Jokenpô com você.
"""

from random import choice
from time import sleep
print("-=-" * 15)
print("VAMOS JOGAR JOKENPÔ?!")
print("-=-" * 15)
sleep(1)

print("No final do Jokenpô você digita se vai jogar Pedra, Papel ou Tesoura.")
sleep(2.5)
print("Jo", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", )
sleep(0.5)
print("Ken", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", )
sleep(0.5)
print("PÔ!!!!!!")
sleep(0.3)

opp = input("VAI: ").capitalize()      #Opção da Pessoa
opc = ["Pedra", "Papel", "Tesoura"]    #Opção do computador
rand = choice(opc)

if opp == rand:
    print("{} VS {}".format(opp, rand))
    print("IXI! HAHA! Dessa vez empatamos! ;D")
elif opp == "Pedra":
    if rand == "Papel":
        print("{} VS {}".format(opp, rand))
        print("Papel engole pedra! AHA! GANHEI DE VOCÊ! =D")
    else:
        print("{} VS {}".format(opp, rand))
        print("Pedra quebra tesoura! Ah! =( VOCÊ ME GANHOU!")
elif opp == "Papel":
    if rand == "Pedra":
        print("{} VS {}".format(opp, rand))
        print("Papel engole pedra! Ah! =( VOCÊ ME GANHOU!")
    else:
        print("{} VS {}".format(opp, rand))
        print("Tesoura corta papel! Ah! =( VOCÊ ME GANHOU!")
elif opp == "Tesoura":
    if rand == "Pedra":
        print("{} VS {}".format(opp, rand))
        print("Pedra quebra tesoura! AHA! GANHEI DE VOCÊ! =D")
    else:
        print("{} VS {}".format(opp, rand))
        print("Tesoura corta papel! Ah! =( VOCÊ ME GANHOU!")


# JEITO QUe fiz da primeira vez:::::

"""if opp == rand:
    print("{} VS {}".format(opp, rand))
    print("IXI! HAHA! Dessa vez empatamos! ;D")
elif opp == "Pedra" and rand == "Papel":
    print("{} VS {}".format(opp, rand))
    print("Papel engole pedra! AHA! GANHEI DE VOCÊ! =D")
elif opp == "Papel" and rand == "Pedra":
    print("{} VS {}".format(opp, rand))
    print("Papel engole pedra! Ah! =( VOCÊ ME GANHOU!")
elif opp == "Pedra" and rand == "Tesoura":
    print("{} VS {}".format(opp, rand))
    print("Pedra quebra tesoura! Ah! =( VOCÊ ME GANHOU!")
elif opp == "Tesoura" and rand == "Pedra":
    print("{} VS {}".format(opp, rand))
    print("Pedra quebra tesoura! AHA! GANHEI DE VOCÊ! =D")
elif opp == "Tesoura" and rand == "Papel":
    print("{} VS {}".format(opp, rand))
    print("Tesoura corta papel! Ah! =( VOCÊ ME GANHOU!")
elif opp == "Papel" and rand == "Tesoura":
    print("{} VS {}".format(opp, rand))
    print("Tesoura corta papel! AHA! GANHEI DE VOCÊ! =D")"""



