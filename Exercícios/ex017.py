""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa. """

from math import hypot
oposto = float(input("Digite o valor do Cateto Oposto: "))
adjacente = float(input("Digite o valor do Cateto Adjacente: "))
hipotenusa = hypot(oposto, adjacente)
print("A Hipotenusa desse triângulo retângulo é: {:.2f}".format(hipotenusa))


