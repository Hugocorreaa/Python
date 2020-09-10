"""

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.

"""

import emoji
from time import sleep

print("-=-" * 20)
print("Os fogos de artifício estão prestes a começar!!!")
print("-=-" * 20)
sleep(1)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
for c in range(0, 20):
    print(emoji.emojize(":fireworks:"), end="")
