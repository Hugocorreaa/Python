# Escreva um programa que converta uma temperatura digitada em ºC e converta em ºF.

celsius = float(input("Informe a temperatura em ºC: "))
fahrenheit = (1.8 * celsius) + 32

print("A temperatura de {}ºC equivale à {}F!".format(celsius, fahrenheit))