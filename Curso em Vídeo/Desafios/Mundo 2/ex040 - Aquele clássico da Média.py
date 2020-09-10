"""Crie um programa que leia duas natas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:

-Média abaixo de 5.0: Reprovado
-Média entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: Aprovado
"""

from time import sleep
print("-=-" * 20)
print("MÉDIA DO ALUNO!")
print("-=-" * 20)
sleep(1)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print("{}REPROVADO!{}".format("\033[1;31m", "\033[m"))
    print("A média do aluno foi: {}".format(media))
elif 5 <= media <= 6.9:
    print("{}RECUPERAÇÃO!{}".format("\033[1;33m", "\033[m"))
    print("A média do aluno foi: {}".format(media))
else:
    print("{}Parabéns! Você foi APROVADO!{}".format("\033[1;34m", "\033[m"))
