'''

Crie um programa onde o usuário possa digitar vários valore numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''

valores = []


while True:
    adicionado = int(input('Digite um valor: '))
    if adicionado not in valores:
        valores.append(adicionado)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar == 'n':
        break
print(sorted(valores))
