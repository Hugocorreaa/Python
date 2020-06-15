# Faça um programa que leia um número inteiro e mostre seu sucessor e antecessor.

numero = int(input("Digite um número inteiro: "))
sucessor = numero + 1
antecessor = numero - 1
print("O antecessor de {} é {} e seu sucessor é {}".format(numero, antecessor, sucessor))
