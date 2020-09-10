""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
 """

numero = int(input("Digite um número inteiro: "))
print("""Escola uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")

conv = int(input("Sua opção: "))

if conv == 1:
    print("{} convertido para BINÁRIO é {}".format(numero,bin(numero)[2:]))
elif conv == 2:
    print("{} convertido para OCTAL é {}".format(numero, oct(numero)[2:]))
elif conv == 3:
    print("{} convertido para HEXADECIMAL é {}".format(numero, hex(numero)[2:]))
else:
    print("{}Opção inválida. Tente novamente!".format("\033[1;31m"))
