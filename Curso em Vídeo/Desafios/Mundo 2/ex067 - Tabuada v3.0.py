'''

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.

'''

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    cont = 0
    print('-' * 20)
    while cont <= 10:
        tabuada = num * cont
        print(f'{num} x {cont:2} = {tabuada}')
        cont += 1
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')