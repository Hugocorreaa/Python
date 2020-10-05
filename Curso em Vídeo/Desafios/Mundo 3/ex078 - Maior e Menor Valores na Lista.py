'''

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

'''

valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))

print('=-' * 30)
print(f'você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for c, v in enumerate(valores):
    if maior == v:
        print(f'{c}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for c, v in enumerate(valores):
    if menor == v:
        print(f'{c}... ', end='')
print()
