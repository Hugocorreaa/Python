'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digit
ar o valor 999, que á a condição de parada. No final, mostre quantos números foram digitados e qual a soma entre eles
(desconsiderando o flag).

'''

print('-=-' * 10)
print('Soma entre valores')
print('-=-' * 10)

#contador = 0
#soma = 0
#n = 0

contador = soma = 0
n = int(input("Digite um número [999 para parar]: "))

while n != 999:
    soma = soma + n
    contador += 1
    n = int(input("Digite um número [999 para parar]: "))
print('Foram digitados {} números e a soma entre eles é {}. '.format(contador, (soma)))
