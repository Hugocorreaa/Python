"""

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.

"""

s = 0
cont = 0
for c in range(1, 501, 2):  # Ele pede o número ímpar. Se de 1 até 501 vai mostrar de 1 até o 500, se
    # pular de 2 em 2 então 1 + 2 = 3, começa do primeiro ímpar.
    if c % 3 == 0:  # Múltiplos de 3 --> Se o numero c for divido por 3 e o resultado é 0
        s += c
        cont += 1  # Está contando quantas vezes o if é acionado.
print("A soma dos {} valores é {}".format(cont, s))
